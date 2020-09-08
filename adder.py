#!/bin/env python3
#code by g1ng3rb1t3 (kevo)
try:
    from telethon.sync import TelegramClient
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
    from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
    from telethon.errors.rpcerrorlist import UserNotMutualContactError
    from telethon.tl.functions.channels import InviteToChannelRequest
    from telethon.errors import SessionPasswordNeededError 
    import configparser
    import os
    import sys
    import csv
    import traceback
    import time
    from time import sleep
    import random
    import colorama
    import progressbar
    from colorama import Fore, Back, Style
    UBlue='\033[4;34m'
    re="\033[1;31m"
    colorama.init(autoreset=True)
    green = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
    reset = Style.RESET_ALL
    white = Style.DIM+Fore.WHITE
    magenta = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
    yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
    red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
    blue = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
    def animated_marker():
        widgets = ['  Starting: ', progressbar.AnimatedMarker()]
        bar = progressbar.ProgressBar(widgets=widgets).start()
        for i in range(50):
            time.sleep(0.10)
            bar.update(i)
    os.system("clear")
    cpass = configparser.RawConfigParser()
    cpass.read('config.data')
    
    try:
        api_id = cpass['cred']['id']
        api_hash = cpass['cred']['hash']
        phone = cpass['cred']['phone']
        client = TelegramClient(phone, api_id, api_hash)
    except KeyError:
        os.system('clear')
        print("{}[{}!{}] {}ERRor".format(blue,red,blue,red))
        sleep(2)
        print("{}[{}!{}] {}Run config.py first".format(blue,red,blue,yellow))
        sys.exit(1)
    animated_marker()
    os.system("toilet --gay -f smblock 'Telegram adder'")
    print(" "*19+"by (g1ng3rb1t3)kevo")
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone, input('{}[+] {}Enter the code: '.format(blue,white)))
        except SessionPasswordNeededError:
            password = input('{}[+] {}Input Your  2factor password>> '.format(blue,white))
            me = client.start(phone,password)
    
    users = []
    with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)
    
    chats = []
    last_date = None
    chunk_size = 200
    groups = []
    
    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)
    
    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue
    print('{}Groups You can add members to'.format(UBlue))
    i = 0
    for group in groups:
        print(blue+'[0'+str(i)+']'+white+ '-> {}{}'.format(red,group.title))
        i += 1
    
    g_index = input("\n{}[+] {}Choose a group to add members>> {}".format(blue,white,green))
    target_group = groups[int(g_index)]
    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
    
    mode = input("{}[=] {}Type 1 to add by username,2 to add by ID> {}".format(blue,white,green))
    n = 0
    try:
        mode = int(mode)
    except ValueError:
        print("{}[{}!{}] {}Invalid. Try again".format(blue,red,blue,red))
        sleep(1)
        exit()
    for user in users:
        n += 1
        if n % 80 == 0:
            sleep(60)
        try:
            print("{}[+] {}Adding {}{}".format(blue,white,green,user['id']))
            if mode == 1:
                if user['username'] == "":
                    continue
                user_to_add = client.get_input_entity(user['username'])
            elif mode == 2:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
            else:
                print("{}[{}!{}] {}Invalid option".format(blue,red,blue,red))
                sleep(2)
                exit()
            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            print("{}[=] {}Please wait".format(blue,green))
            time.sleep(random.randrange(0, 5))
        except PeerFloodError:
            print("{}[{}!{}] {}Flood Error,Try again.".format(blue,red,blue,red))
        except UserPrivacyRestrictedError:
            print("{}[{}!{}] {}User privacy restriction.skipped".format(blue,red,blue,red))
            time.sleep(random.randrange(0, 5))
        except UserNotMutualContactError:
           print("{}[{}!{}] {}User not a mutual contact. Skipped".format(blue,red,blue,red))
           time.sleep(random.randrange(0, 5))
        except KeyboardInterrupt:
            print("\n")
            print("{}[+] {}Closing".format(blue,yellow))
            sleep(1)
            print("{}[+] {}Created by g1ng3rb1t3".format(blue,red))
            print("{}[=] {}https://t.me/Iamk3lv1n".format(blue,red))
            sleep(1)
            sys.exit()
except FileNotFoundError:
    print('{}[{}!{}] {}Found no members to add'.format(blue,red,blue,red))
    sleep(1)
    print('{}[{}!{}] {}Run scrapper.py first to get members'.format(blue,red,blue,green))
    sleep(2)
    exit()
except ConnectionError:
    print("{}[{}!{}] {}Failed to connect to telegram 5 times".format(blue,red,blue,red))
    sleep(2)
    print("\a{}[{}X{}] {}Check your connection".format(blue,red,blue,red))
    sleep(2)
except KeyboardInterrupt:
    print("\n")
    print("{}[+] {}Closing".format(blue,yellow))
    sleep(1)
    print("{}[+] {}Created by g1ng3rb1t3".format(blue,red))
    print("{}[=] {}https://t.me/Iamk3lv1n\a\a".format(blue,red))
    sleep(1)
    sys.exit()