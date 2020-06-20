import requests, os, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

class style():
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

# Global variables
urls = []
processes = []
extensions = []


# Get status code
def download_file(url):
    html = requests.get(url, stream=True)
    return html.status_code, url


def makeURL(wordlistPath, url, extensions):
    global urls
    print(style.YELLOW('\n[*]') + style.RESET(f' Generatnig all URL possibilies from {wordlistPath}, please wait...'))
    with open(wordlistPath, 'r') as f:
        for l in f:
            l = l.strip()
            for e in extensions:
                if url[-1] != "/":
                    fileURL = url + "/" + l + "." + e
                    dirURL = url + "/" + l + "/"
                    dirFileURL = url + "/" + l + "/" + l + "." + e
                    urls.append(fileURL)
                    urls.append(dirURL )
                    urls.append(dirFileURL )


                else:
                    fileURL = url + l + "." + e
                    dirURL = url + l + "/"
                    dirFileURL = url + "/" + l + "/" + l + "." + e
                    urls.append(fileURL)
                    urls.append(dirURL)
                    urls.append(dirFileURL )
    urls = list(dict.fromkeys(urls))
    print(style.GREEN('[+]') + style.RESET(f' Generated {len(urls)} urls to bruteforce.'))

# Main function
def STBuster_():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    url = str(input(style.GREEN('[+]') + style.RESET(' Enter the website URL [eg: http://10.10.10.188/]: ')))
    wordlistPath = str(input(style.GREEN('[+]') + style.RESET(f' Enter the brute force worlist [You are in {os.getcwd()}]: ')))
    exts = str(input(style.GREEN('[+]') + style.RESET(' Enter file extensions seperated by commas [eg: php,html,js]: ')))
    extensions.extend(exts.split(','))
    threads = int(input(style.GREEN('[+]') + style.RESET(' Enter amount of threads you want to use [Default: 10]: ')))

    if not os.path.exists(wordlistPath):
        print(style.RED('[!]') + style.RESET(' Wordlist file is not in path.'))
        sys.exit()

    makeURL(wordlistPath, url, extensions)
    tic = time.perf_counter()

    print(style.YELLOW('\n[*]') + style.RESET(' Starting bruteforce...\n'))
    with ThreadPoolExecutor(max_workers = threads) as executor:
        for url in urls:
            try:
                future = executor.submit(download_file, url)
                result = future.result()
                if result[0] != 404:
                    print(style.GREEN(f'     [{result[0]}]') + style.RESET(f' : {result[1]}'))
            except KeyboardInterrupt:
                print(style.RED('\n[!]') + style.RESET(' User exit.'))
                sys.exit()

    toc = time.perf_counter()
    print(style.GREEN('\n[+]') + style.RESET(f' Scan done: Scanned in {toc - tic:0.2f} seconds.'))
    input(style.YELLOW('\n[!]') + style.RESET(' Press anything to go back to main menu.'))
