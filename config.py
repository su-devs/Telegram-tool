#!/bin/env python3
#code by g1ng3rb1t3 (kevo)
try:
    import os
    from time import sleep
    import colorama
    import sys
    import configparser
    os.system('clear')
    os.system("toilet --gay -f smblock 'Telegram tool'")
    print(" "*17+"by (g1ng3rb1t3)kevo")
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    green = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
    reset = Style.RESET_ALL
    white = Style.DIM+Fore.WHITE
    magenta = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
    yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
    red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
    blue = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
    os.system("touch config.data")
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    apid = input("{}[+] {}Enter api ID>> {}".format(blue,white,green))
    cpass.set('cred', 'id', apid)
    hashid = input("{}[+] {}Enter hash ID>> {}".format(blue,white,green))
    cpass.set('cred', 'hash', hashid)
    phone = input("{}[+] {}Enter phone number>> {}".format(blue,white,green))
    cpass.set('cred', 'phone', phone)
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    print('{}[+] {}Setup complete'.format(blue,green))
    sleep(1)
    print('{}[+] {}Now open scrapper.py to fetch members'.format(blue,green))
except KeyboardInterrupt:
    print("\n")
    print("{}[+] {}Closing".format(blue,yellow))
    sleep(1)
    print("{}[+] {}Created by g1ng3rb1t3".format(blue,red))
    print("{}[=] {}https://t.me/Iamk3lv1n\a\a".format(blue,red))
    sleep(1)
    sys.exit()