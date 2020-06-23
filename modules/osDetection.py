import nmap3, sys, time, style

def osDetection():
    print (u"{}[2J{}[;H".format(chr(27), chr(27)))
    host = str(input(style.GREEN('[+]') + style.RESET(' Enter the machine IP address [eg: 10.10.10.188]: ')))
    print(style.GREEN('[+]') + style.RESET(' Scanning the host...'))
    tic = time.perf_counter()
    nmScan = nmap3.NmapScanTechniques()
    try:
        data = nmScan.nmap_os_detection(host)
    except:
        print(style.RED('[!]') + style.RESET('Error 00-80: Cannot reach the host.'))


    print(style.GREEN('\n[+]') + style.RESET(f' Host: {host}'))
    print(style.GREEN('[+]') + style.RESET(' OS detection possibilities:'))

    oss = len(data)

    for os in range(0,oss):
        try:
            print(style.GREEN('\n[+]') + style.RESET(f' OS Name: {data[os]["name"]}'))
        except:
            print(style.GREEN('\n[+]') + style.RESET(' OS Name: Not found.'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' Accuracy: {data[os]["accuracy"]}%'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' Accuracy: Not found.'))
        try:

            print(style.YELLOW('    [-]') + style.RESET(f' Type: {data[os]["osclass"]["type"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' Type: not found.'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' OS Family: {data[os]["osclass"]["osfamily"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' OS Family: Not found.'))
        try:
            print(style.YELLOW('    [-]') + style.RESET(f' OS Generation: {data[os]["osclass"]["osgen"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' OS Generation: Not found.'))

        try:
            print(style.YELLOW('    [-]') + style.RESET(f' OS CPE: {data[os]["cpe"]}'))
        except:
            print(style.YELLOW('    [-]') + style.RESET(' OS CPE: Not found.'))



    toc = time.perf_counter()
    print(style.GREEN('\n[+]') + style.RESET(f' Scan done: 1 IP address (1 host up) scanned in {toc - tic:0.2f} seconds.'))
    input(style.YELLOW('\n[!]') + style.RESET(' Press anything to go back to main menu.'))
