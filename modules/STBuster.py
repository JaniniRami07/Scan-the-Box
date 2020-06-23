import requests, os, sys, time
from modules.style import Style
from concurrent.futures import ThreadPoolExecutor, as_completed

# Global variables
urls = []
processes = []
extensions = []


# Get status code
def download_file(url):
    html = requests.get(url, stream=True)
    return html.status_code, url


def make_url(wordlistPath, url, extensions):
    global urls
    print(Style.YELLOW('\n[*]') + Style.RESET(f' Generatnig all URL possibilies from {wordlistPath}, please wait...'))
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
    print(Style.GREEN('[+]') + Style.RESET(f' Generated {len(urls)} urls to bruteforce.'))

# Main function
def stbuster():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    while True:
        url = str(input(Style.GREEN('[+]') + Style.RESET(' Enter the website URL [eg: http://10.10.10.188/]: ')))
        if len(url) != 0:
            break
        else:
            print(Style.RED('[-]') + Style.RESET(' URL can\'t be blank!'))
    wordlistPath = str(input(Style.GREEN('[+]') + Style.RESET(f' Enter the brute force worlist [You are in {os.getcwd()}]: ')))
    exts = str(input(Style.GREEN('[+]') + Style.RESET(' Enter file extensions seperated by commas [eg: php,html,js]: ')))
    extensions.extend(exts.split(','))
    while True:
        try:
            threads = int(input(Style.GREEN('[+]') + Style.RESET(' Enter amount of threads you want to use [Default: 10]: ')))
            break
        except:
            print(Style.RED('[-]') + Style.RESET(' Enter a number! '))
            continue
    
    if not os.path.exists(wordlistPath):
        print(Style.RED('[!]') + Style.RESET(' Wordlist file is not in path.'))
        sys.exit()

    make_url(wordlistPath, url, extensions)
    tic = time.perf_counter()

    print(Style.YELLOW('\n[*]') + Style.RESET(' Starting bruteforce...\n'))
    with ThreadPoolExecutor(max_workers = threads) as executor:
        for url in urls:
            try:
                future = executor.submit(download_file, url)
                result = future.result()
                if result[0] != 404:
                    print(Style.GREEN(f'     [{result[0]}]') + Style.RESET(f' : {result[1]}'))
            except KeyboardInterrupt:
                print(Style.RED('\n[!]') + Style.RESET(' User exit.'))
                sys.exit()

    toc = time.perf_counter()
    print(Style.GREEN('\n[+]') + Style.RESET(f' Scan done: Scanned in {toc - tic:0.2f} seconds.'))
    input(Style.YELLOW('\n[!]') + Style.RESET(' Press enter to go back to main menu.'))
