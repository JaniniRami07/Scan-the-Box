import nmap3, sys, time

class style():
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

def portScan():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    host = str(input(style.GREEN('[+]') + style.RESET(' Enter the machine IP address [eg: 10.10.10.188]: ')))
    print(style.GREEN('[+]') + style.RESET(' Scanning the host...'))
    tic = time.perf_counter()
    nmScan = nmap3.NmapScanTechniques()
    try:
        data = nmScan.nmap_syn_scan(host, args='-A')
    except:
        print(style.RED('[!]') + style.RESET('Error 00-80: Cannot reach the host.'))


    print(style.GREEN('\n[+]') + style.RESET(f' Host: {host}'))
    print(style.GREEN('[+]') + style.RESET(' Open Ports:'))

    ports = len(data[host])

    for port in range(0,ports):
        print(style.GREEN('\n[+]') + style.RESET(f' {data[host][port]["portid"]}/{data[host][port]["protocol"]}:'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' Port Name: {data[host][port]["service"]["name"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' Port Name: Not found.'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' Port Product: {data[host][port]["service"]["product"]}'))
        except :
            print(style.YELLOW('    [-]') + style.RESET(' Port Product: Not found.'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' Product Version: {data[host][port]["service"]["version"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' Product Version: Not found.'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' Extra Info: {data[host][port]["service"]["extrainfo"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' Extra Info: Not found.'))

    toc = time.perf_counter()
    print(style.GREEN('\n[+]') + style.RESET(f' Scan done: 1 IP address (1 host up) scanned in {toc - tic:0.2f} seconds.'))
    input(style.YELLOW('\n[!]') + style.RESET(' Press anything to go back to main menu.'))
