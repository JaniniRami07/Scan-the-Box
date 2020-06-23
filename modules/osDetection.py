import nmap3, sys, time
from modules.style import Style

def os_detection():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    host = str(input(Style.GREEN('[+]') + Style.RESET(' Enter the machine IP address [eg: 10.10.10.188]: ')))
    print(Style.GREEN('[+]') + Style.RESET(' Scanning the host...'))
    tic = time.perf_counter()
    nmScan = nmap3.NmapScanTechniques()
    try:
        data = nmScan.nmap_os_detection(host)
    except:
        print(Style.RED('[!]') + Style.RESET('Error 00-80: Cannot reach the host.'))
        input(Style.YELLOW('\n[!]') + Style.RESET(' Press enter to go back to main menu.'))
        return 0
    
    oss = len(data)

    print(Style.GREEN('\n[+]') + Style.RESET(f' Host: {host}'))
    print(Style.GREEN('[+]') + Style.RESET(' OS detection possibilities:'))

    for os in range(0,oss):
        try:
            print(Style.GREEN('\n[+]') + Style.RESET(f' OS Name: {data[os]["name"]}'))
        except:
            print(Style.GREEN('\n[+]') + Style.RESET(' OS Name: Not found.'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' Accuracy: {data[os]["accuracy"]}%'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' Accuracy: Not found.'))
        try:

            print(Style.YELLOW('    [-]') + Style.RESET(f' Type: {data[os]["osclass"]["type"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' Type: not found.'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' OS Family: {data[os]["osclass"]["osfamily"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' OS Family: Not found.'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' OS Generation: {data[os]["osclass"]["osgen"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' OS Generation: Not found.'))

        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' OS CPE: {data[os]["cpe"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' OS CPE: Not found.'))



    toc = time.perf_counter()
    print(Style.GREEN('\n[+]') + Style.RESET(f' Scan done: 1 IP address (1 host up) scanned in {toc - tic:0.2f} seconds.'))
    input(Style.YELLOW('\n[!]') + Style.RESET(' Press enter to go back to main menu.'))
