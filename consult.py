#!usr/bin/env python3

try:
    from modules.modules import *
    from sys import argv
except Exception as e:
    print(f'An error with a module has occurred: {e}')
else:
    print('\n\033[34mCoded by f4ll_py\033[m')
    print('\n\033[34mVersion: 0.2\033[m')
    print('''\n\033[31m     ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗
    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝
    ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   
    ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   
    ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   
     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝\033[m''')
    if len(argv) >= 2:
        if argv[1] == '':
            print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')
        elif argv[1] == '-h' or argv[1] == '--help':
            print('\n[+] Basic Commands:\n')
            print('[+]   -h                 Help')
            print('[+]   --help             Help')
            print('[+]   --cep              CEP Consult')
            print('[+]   --cnpj             CNPJ Consult')
        elif argv[1] == '--cep':
            if len(argv) >= 3:
                if argv[2] != '':
                    target = argv[2]
                else:
                    print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')
                if target != '':
                    consultCEP(target)
            else:
                print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')
        elif argv[1] == '--cnpj':
            if len(argv) >= 3:
                if argv[2] != '':
                    target = argv[2]
                else:
                    print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')
                if target != '':
                    consultCNPJ(target)
            else:
                print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')
        else:
            print('\n\033[31m[-] Incorrect parameter. Enter "-h" or "--help" to view valid parameters.\033[m')
    else:
        print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')
