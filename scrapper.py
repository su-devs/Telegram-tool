#!/bin/env python3
#code by g1ng3rb1t3 (kevo)
try:
    from telethon.sync import TelegramClient
    from telethon.tl.functions.messages import GetDialogsRequest
    from telethon.tl.types import InputPeerEmpty
    from telethon.errors import SessionPasswordNeededError
    import os, sys
    import configparser
    import progressbar
    import csv
    import time
    from time import sleep
    import colorama
    UBlue='\033[4;34m'
    from colorama import Fore, Back, Style
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
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone, input('{}[+] {}Enter the code>> {}'.format(blue,white,green)))
        except SessionPasswordNeededError:
            password = input('{}[+] {}Input Your  2factor password>> {}'.format(blue,white,green))
            me = client.start(phone,password)
    
    os.system('clear')
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
     
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)
     
    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue
    animated_marker()
    os.system("toilet --gay -f smblock 'Telegram scrapper'")
    print(" "*27+"by (g1ng3rb1t3)kevo")
    print('{}Groups you can fetch members from'.format(UBlue))
    i=0
    for g in groups:
        print(blue+'[0'+str(i)+']'+white+ '-> {}{}'.format(red,g.title))
        i+=1
    
    g_index = int(input("\n{}[+] {}Choose a group to fetch members>> {}".format(blue,white,green)))
    target_group=groups[int(g_index)]
     
    print('{}[+] {}Fetching Members...'.format(blue,green))
    time.sleep(1)
    all_participants = []
    all_participants = client.get_participants(target_group, aggressive=True)
     
    print('{}[+] {}Saving In file...'.format(blue,green))
    time.sleep(1)
    with open("members.csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
        for user in all_participants:
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name= (first_name + ' ' + last_name).strip()
            writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
    print('{}[+] {}Members fetched successfully'.format(blue,green))
except ValueError:
    print('\a{}[{}!{}] {}Invalid. Try again'.format(blue,red,blue,red))
    sleep(2)
except EOFError:
    print('{}[{}!{}] {}Error'.format(blue,red,blue,red))
    sleep(2)
    exit()
except KeyboardInterrupt:
    print("\n")
    print("{}[+] {}Closing".format(blue,yellow))
    sleep(1)
    print("{}[+] {}Created by g1ng3rb1t3".format(blue,red))
    print("{}[=] {}https://t.me/Iamk3lv1n\a\a".format(blue,red))
    sleep(1)
    sys.exit()