import nmap3, sys, time
from modules.style import Style

def port_scan():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    while True:
        host = str(input(Style.GREEN('[+]') + Style.RESET(' Enter the machine IP address [eg: 10.10.10.188]: ')))
        if len(host) != 0:
            break
        else:
            print(Style.RED('[-]') + Style.RESET(' IP Address can\'t be empty! '))
    
    print(Style.GREEN('[+]') + Style.RESET(' Scanning the host...'))
    tic = time.perf_counter()
    nmScan = nmap3.NmapScanTechniques()
    try:
        data = nmScan.nmap_syn_scan(host, args='-A')
    except:
        print(Style.RED('[!]') + Style.RESET('Error 00-80: Cannot reach the host.'))


    print(Style.GREEN('\n[+]') + Style.RESET(f' Host: {host}'))
    print(Style.GREEN('[+]') + Style.RESET(' Open Ports:'))

    ports = len(data[host])

    for port in range(0,ports):
        print(Style.GREEN('\n[+]') + Style.RESET(f' {data[host][port]["portid"]}/{data[host][port]["protocol"]}:'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' Port Name: {data[host][port]["service"]["name"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' Port Name: Not found.'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' Port Product: {data[host][port]["service"]["product"]}'))
        except :
            print(Style.YELLOW('    [-]') + Style.RESET(' Port Product: Not found.'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' Product Version: {data[host][port]["service"]["version"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' Product Version: Not found.'))
        try:
            print(Style.YELLOW('    [-]') + Style.RESET(f' Extra Info: {data[host][port]["service"]["extrainfo"]}'))
        except:
            print(Style.YELLOW('    [-]') + Style.RESET(' Extra Info: Not found.'))

    toc = time.perf_counter()
    print(Style.GREEN('\n[+]') + Style.RESET(f' Scan done: 1 IP address (1 host up) scanned in {toc - tic:0.2f} seconds.'))
    input(Style.YELLOW('\n[!]') + Style.RESET(' Press enter to go back to main menu.'))
