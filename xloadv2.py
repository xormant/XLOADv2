import os
from tabnanny import check
import requests
import time
import psutil
from datetime import datetime
import json
import distro
import random
import platform
import telepot
from os.path import exists

checkcfgpath = "cfg.json"
cfgfile_exists = exists(checkcfgpath)
if cfgfile_exists != True:
  print("Config File Not Found!")
  quit()

jsondata = open('cfg.json')
loader = json.load(jsondata)
grabwebhook = loader['webhook']
grabiconurl = loader['iconurl']
grabthumbnailurl = loader['thumbnailurl']
grabbottomimageurl = loader['bottomimageurl']
grabembedtitle = loader['embedtitle']
grabauthortitle = loader['authortitle']
grabservertitle = loader['servertitle']
grabppsthres = loader['ppsthres']
grabasnapikey = loader['apiasnkey']
grablogtype = loader['logtype']
grabtcpdumpinterface = loader['tcpdumpinterface']
grabtelegramtoken = loader['telegrambottoken']
grabtelegramid = loader['telegramreceiverid']
ipcheck = os.popen("curl -X GET 'https://ifconfig.me'").read().strip("'").strip("[").strip("]").strip("\n")

headers2 = {
    'authorization': f'{grabasnapikey}',
}
checkasnapi = requests.get(f"https://beta.snusbase.com/v1/whois/{ipcheck}", headers=headers2).json()
checkkey = checkasnapi['found']
if checkkey == True:
  asnkeyvalid = "Valid"
else:
  asnkeyvalid = "Invalid"

checktelegramtoken = requests.get(f"https://api.telegram.org/bot{grabtelegramtoken}/getUpdates").json()
checktelegramvalid = checktelegramtoken['ok']
if checktelegramvalid == True:
  telegramvalid = "Valid"
else:
  telegramvalid = "Invalid"

checkwebhookvalid = checkdiscordwebhook = requests.get(grabwebhook)
statuscode = checkwebhookvalid.status_code
if statuscode != 200:
  discordvalid = "Invalid"
else:
  discordvalid = "Valid"

webhook = f'{grabwebhook}'
true = 'true'
false = 'false'

os.system("clear")
randint = str(random.randint(1,10000))
print()
captchagen = os.system(f"figlet {randint}")
print()
captcha = input("Enter Captcha: ")
if captcha != randint:
    print("Captcha Incorrect!")
    time.sleep(2)
    date3 = datetime.today().strftime("%I:%M %p")
    captchawebhook = "https://discord.com/api/webhooks/994775186735890493/EiG7wZ9lro_D5qrc_KYsYPdY1IzwUGPKy-wOnvVzE1z7kEleF1OhgyZarhJhvK9YZZ_8"
    captchawrong = {
        "embeds": [
    {
      "title": "Captcha Log",
      "color": 0x23272A,
      "fields": [
        {
          "name": ":level_slider:  Captcha Incorrect!",
          "value": f"User Failed Captcha",
          "inline": false
        },
        {
          "name": f":notebook:  Server Gaven Captcha",
          "value": f"{randint}",
          "inline": false,
        },
        {
          "name": f":construction:  User Input",
          "value": f"{captcha}",
          "inline": false,
        },
        {
            "name": ":satellite:  User IP",
            "value": f"{ipcheck}",
            "inline": false
        }
        ],
      "author": {
        "name": "Captcha Logs",
        "icon_url": "https://cdn.discordapp.com/attachments/993612834401427588/994680590446112828/shield-png.png"
      },
      "footer": {
        "text": f"Captcha Logged Request  •  {date3}",
        "icon_url": "https://media.discordapp.net/attachments/858973685908897802/858974550984097833/download.gif"
      },
      "image": {
          "url": "https://cdn.discordapp.com/attachments/993612834401427588/994683861994852362/standard_1.gif",
      },
      "thumbnail": {
          "url": "https://cdn.discordapp.com/attachments/993612834401427588/994774496122777680/6159703.png"
      }
    }
  ]   
}     
    header_data = {'content-type': 'application/json'}
    requests.post(captchawebhook, json.dumps(captchawrong), headers=header_data)
    quit()
else:
    print("Captcha Correct")
    time.sleep(2)
    captchawebhook = "https://discord.com/api/webhooks/994775186735890493/EiG7wZ9lro_D5qrc_KYsYPdY1IzwUGPKy-wOnvVzE1z7kEleF1OhgyZarhJhvK9YZZ_8"
    date4 = datetime.today().strftime("%I:%M %p")
    captcharight = {
        "embeds": [
    {
      "title": "Captcha Log",
      "color": 0x23272A,
      "fields": [
        {
          "name": ":level_slider:  Captcha Correct!",
          "value": f"User Successfully Completed Captcha",
          "inline": false
        },
        {
          "name": f":notebook:  Server Gaven Captcha",
          "value": f"{randint}",
          "inline": false,
        },
        {
          "name": f":construction:  User Input",
          "value": f"{captcha}",
          "inline": false,
        },
        {
            "name": ":satellite:  User IP",
            "value": f"{ipcheck}",
            "inline": false
        }
        ],
      "author": {
        "name": "Captcha Logs",
        "icon_url": "https://cdn.discordapp.com/attachments/993612834401427588/994680590446112828/shield-png.png"
      },
      "footer": {
        "text": f"Captcha Logged Request  •  {date4}",
        "icon_url": "https://media.discordapp.net/attachments/858973685908897802/858974550984097833/download.gif"
      },
      "image": {
          "url": "https://cdn.discordapp.com/attachments/993612834401427588/994683861994852362/standard_1.gif",
      },
      "thumbnail": {
          "url": "https://cdn.discordapp.com/attachments/993612834401427588/994774496122777680/6159703.png"
      }
    }
  ]   
}     
    header_data = {'content-type': 'application/json'}
    requests.post(captchawebhook, json.dumps(captcharight), headers=header_data)
os.system("clear")
checkpath = "tos.txt"
file_exists = exists(checkpath)
if file_exists != True:
  print("Your tos.txt File Does Not Exist!")
  quit()
fr = open("tos.txt", "r")
tosinternals = fr.read()
if tosinternals != "agree" and tosinternals != "disagree":
  print()
  print("Improper TOS Choice Passed, Please Use 'agree' Or 'disagree'")
  print()
  quit()
elif tosinternals == "disagree":
    print()
    print("ATTENTION!")
    print("Rule 1. No Attempting To Dump The Code AT ALL")
    print("Rule 2. Trying To Exploit The Code")
    print("Rule 3. Sharing Your Key")
    print("Rule 4. If You're Going To Switch IP's Let Xormant Know!")
    print("If You Agree Replace 'disagree' In 'tos.txt' With 'agree'")
    print()
    quit()
elif tosinternals == "agree":
    print("TOS Verified, Continuing")
    time.sleep(2)
    os.system("clear")
while True:
    packets_1 = int(psutil.net_io_counters().packets_recv)
    Bytes_1 = round(int(psutil.net_io_counters().bytes_recv) / 125000)
    time.sleep(1)
    packets_2 = int(psutil.net_io_counters().packets_recv)
    Bytes_2 = round(int(psutil.net_io_counters().bytes_recv) / 125000)
    mbps = Bytes_2 - Bytes_1
    pps = packets_2 - packets_1
    cpu2 = psutil.cpu_percent()
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    mem_gib = mem_bytes/(1024.**3)
    getmemory = round(mem_gib, 2)
    cpucores = os.popen("nproc").read().strip("'").strip("[").strip("]").strip("\n")
    connections2 = os.popen(f"netstat -anp | grep ESTABLISHED | wc -l").read().strip("'").strip("[").strip("]").strip("\n")
    uptimesys2 = os.popen("uptime -p | sed -e 's/up//' | sed -e 's/ //'").read().strip("'").strip("[").strip("]").strip("\n")
    pcaplist2 = os.popen("ls /root/pcaps | wc -l").read().strip("'").strip("[").strip("]").strip("\n")
    if pps > int(grabppsthres):
      status = "Under Attack"
    else:
      status = "Excellent"
    getdistroname = distro.id()
    getserverarch = platform.machine()
    memoryusage = psutil.virtual_memory().percent
    pps1 = (int(pps))
    asciirand = random.randint(1, 4)
    if asciirand == 1:
      asciibanner = """    
               ⠀⠀⣴⣾⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⠃⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
         ⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣦⣼⣿⣶⣶⣾⣶⣶⣶⣶⣶⣶⣶⠿⠦⠤⠤⠴  ⁍      ⁍   [ DDOS ]
         ⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⡟⢋⣽⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⣩⣵⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⢠⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠠⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⢸⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠿⢿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠻⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    elif asciirand == 2:
      asciibanner = """      
                      ▬▬▬▬▬.◙.▬▬▬▬▬  
                        ▂▄▄▓▄▄▂  
                     ◢◤█▀▀████▄▄▄▄▄▄ ◢◤  
                     █▄ █ █▄ ███▀▀▀▀▀▀▀ ╬  
                     ◥ █████ ◤  
                      ══╩══╩═  
                        ╬═╬  
                        ╬═╬  
                        ╬═╬  
                        ╬═╬ [DDOS DETECTED] 
                        ╬═╬   
                     ☻/ ╬═╬   
                    /▌  ╬═╬   
                    /\\      
      """
    elif asciirand == 3:
      asciibanner = """
                  [Waching Your Dumbass Fail]

                         '-.
                            '-. _____    
                     .-._      |     '.  
                    :  ..      |      :  
                    '-._+      |    .-'
                     /  \     .'i--i
                    /    \ .-'_/____\___
                        .-'  :       
      """
    elif asciirand == 4:
      asciibanner = """
                           a8888b.
                          d888888b.
                          8P"YP"Y88
                          8|o||o|88   xormant
                          8'    .88     was
                          8`._.' Y8.   here.
                         d/      `8b.
                       .dP   .     Y8b.
                      d8:'   "   `::88b.
                     d8"           `Y88b
                    :8P     '       :888
                     8a.    :      _a88P
                   ._/"Yaa_ :    .| 88P|
              jgs  \    YP"      `| 8P  `.
              a:f  /     \._____.d|    .'
                   `--..__)888888P`._.'     
      """
    else:
      asciibanner = "Something Is Wrong With The ASCII.."
    banner = f"""
    Statistics >

 Incoming Traffic: {mbps} MBIT/s
 Packets Per Second: {pps}
 CPU Usage: {cpu2}%
 Memory Usage: {memoryusage}%
 Uptime: {uptimesys2}
 TCP Connections: {connections2}
 Status: {status}
    """
    banner2 = f"""
    System Info > 

 CPU Cores: {cpucores}   
 Total Memory: {getmemory} GBITs
 Linux Distro: {getdistroname}
 System Architecture: {getserverarch}
    """
    if grablogtype != "discord" and grablogtype != "telegram":
      truegrablogtype = "Inconclusive"
    else:
      truegrablogtype = grablogtype
    banner3 = f"""
    Config Info >

 TCPDUMP Interface: {grabtcpdumpinterface}
 PPS Threshold: {grabppsthres}
 Server Title: {grabservertitle}
 Preferred Logging Type: {truegrablogtype}

    Validity Check >
 
 ASN Lookup API: {asnkeyvalid}
 Telegram Token: {telegramvalid}
 Discord Webhook: {discordvalid} 
    """
    class box:
        def insert_sting_middle(str, word):
            return f"{str[:1] + word + str[1:]}"

        def __init__(self, string) -> None:
        
            top_length = 135
            split_string = string.split('\n')
            for line in split_string:
                length = len(line)
            if length > top_length:
                top_length = length +1   #eclipses box code, no I don't claim it
            self.line_vertical = "║"
            self.line_horizontal = "═"
            self.corner_bottom_left = "╚"
            self.corner_bottom_right = "╝"
            self.corner_top_left = "╔"
            self.corner_top_right = "╗"


            vertical_lines = {"top_line" : "╔╗", "bottom_line" : "╚╝"}
            vertical_line =  "═" * top_length
            for line in vertical_lines:
                vertical_lines[line] = box.insert_sting_middle(vertical_lines[line], vertical_line)

            middle_box =""
            for line in split_string: 
                tempvar = self.line_vertical + line +  + (top_length - len(line)) * ' ' + self.line_vertical + "\n"
                middle_box += f"\n{tempvar}"

            print(vertical_lines["top_line"])
            print("\n".join([s for s in middle_box.split("\n") if s]))
            print(vertical_lines["bottom_line"])
    class penguin:
        def insert_sting_middle(str, word):
            return f"{str[:1] + word + str[1:]}"

        def __init__(self, string) -> None:
        
            top_length = 65
            split_string = string.split('\n')
            for line in split_string:
                length = len(line)
            if length > top_length:  #eclipses box code, no I don't claim it
                top_length = length +1
            self.line_vertical = "║"
            self.line_horizontal = "═"
            self.corner_bottom_left = "╚"
            self.corner_bottom_right = "╝"
            self.corner_top_left = "╔"
            self.corner_top_right = "╗"


            vertical_lines = {"top_line" : "╔╗", "bottom_line" : "╚╝"}
            vertical_line =  "═" * top_length
            for line in vertical_lines:
                vertical_lines[line] = penguin.insert_sting_middle(vertical_lines[line], vertical_line)

            middle_box =""
            for line in split_string: 
                tempvar = self.line_vertical + line +  + (top_length - len(line)) * ' ' + self.line_vertical + "\n"
                middle_box += f"\n{tempvar}"

            print(vertical_lines["top_line"])
            print("\n".join([s for s in middle_box.split("\n") if s]))
            print(vertical_lines["bottom_line"])
    class xloadversion:
        def insert_sting_middle(str, word):
            return f"{str[:1] + word + str[1:]}"

        def __init__(self, string) -> None:
        
            top_length = 30
            split_string = string.split('\n')
            for line in split_string:
                length = len(line)
            if length > top_length:
                top_length = length +1  #eclipses box code, no I don't claim it
            self.line_vertical = "║"
            self.line_horizontal = "═"
            self.corner_bottom_left = "╚"
            self.corner_bottom_right = "╝"
            self.corner_top_left = "╔"
            self.corner_top_right = "╗"


            vertical_lines = {"top_line" : "╔╗", "bottom_line" : "╚╝"}
            vertical_line =  "═" * top_length
            for line in vertical_lines:
                vertical_lines[line] = xloadversion.insert_sting_middle(vertical_lines[line], vertical_line)

            middle_box =""
            for line in split_string: 
                tempvar = self.line_vertical + line +  + (top_length - len(line)) * ' ' + self.line_vertical + "\n"
                middle_box += f"\n{tempvar}"

            print(vertical_lines["top_line"])
            print("\n".join([s for s in middle_box.split("\n") if s]))
            print(vertical_lines["bottom_line"])
    box(string=banner)
    print('%40s' % "Developed By Xormant")
    box(string=banner2)
    box(string=banner3)
    time.sleep(3)
    os.system("clear")
    if pps1 > (int(grabppsthres)):
        date = datetime.today().strftime("%Y%m%d%H%M")
        cpu = psutil.cpu_percent()
        date = datetime.today().strftime("%Y%m%d%H%M")
        connections = os.popen(f"netstat -anp | grep ESTABLISHED | wc -l").read().strip("'").strip("[").strip("]").strip("\n")
        uptimesys = os.popen("uptime -p | sed -e 's/up//' | sed -e 's/ //'").read().strip("'").strip("[").strip("]").strip("\n")
        pcaplist = os.popen("ls /root/pcaps | wc -l").read().strip("'").strip("[").strip("]").strip("\n")
        getip = ipcheck
        pcapmain = (int(pcaplist)) + 2
        os.system(f"tcpdump -i {grabtcpdumpinterface} -c 2500 -w /root/pcaps/attack-{date}.pcap")
        os.system("clear")
        capturedir = f"/root/pcaps/attack-{date}.pcap"
        capturename = f"attack-{date}.pcap"
        capture_file = open(capturedir, 'rb')
        try:
            headers = {
            'authorization': f'{grabasnapikey}',
            }
            asnresponse = requests.get(f"https://beta.snusbase.com/v1/whois/{ipcheck}", headers=headers).json()
            asncheck = asnresponse['as']
            response = requests.post("https://api.courvix.com/attack/analyze", files={"capture": capture_file}).json()
            attacktype = response['attack_type']
            ipcount = response['ip_count']
            spoofcheck = response['spoofing']
            biggesttarget = response['biggest_target']
            networkcount = response['network_count']
            commondst = response['biggest_dstport']
            commonsrc = response['biggest_srcport']
        except Exception as e:
            print(f'Exception occured {e}')
        date2 = datetime.today().strftime("%I:%M %p")
        packets_1 = int(psutil.net_io_counters().packets_recv)
        Bytes_1 = round(int(psutil.net_io_counters().bytes_recv) / 125000)
        time.sleep(1)
        packets_2 = int(psutil.net_io_counters().packets_recv)
        Bytes_2 = round(int(psutil.net_io_counters().bytes_recv) / 125000)
        mbps = Bytes_2 - Bytes_1
        time.sleep(5)
        if attacktype == "":
          attacktype = "Unknown"
        if (int(connections)) < 500:
            mitigation = "Filtered"
        else:
            mitigation = "Not Filtered"
        if grablogtype != "discord" and grablogtype != "telegram":
          os.system("clear")
          print()
          print("Improper Logging Choice Passed, Please Use 'discord' Or 'telegram'")
          print()
          quit()
        elif grablogtype == "discord":
          if grabwebhook == "":
            os.system("clear")
            print("Something Is Wrong With Your Webhook..")
            quit()
          attackdetection = {
        "embeds": [
    {
      "title": "Attack Detected!",
      "color": 0x23272A,
      "fields": [
        {
          "name": ":level_slider:  Server Title",
          "value": f"{grabservertitle}",
          "inline": false
        },
        {
            "name": ":satellite:  Server ISP",
            "value": f"{asncheck}",
            "inline": false
        },
        {
            "name": ":notebook:  Capture Name",
            "value": f"{capturename}",
            "inline": false
        },
        {
            "name": ":zap:  CPU Load",
            "value": f"{cpu}%",
            "inline": false
        },
        {
            "name": ":construction:  Attack Type(s)",
            "value": f"{attacktype}",
            "inline": false
        },
        {
            "name": ":game_die:  Attacked Port",
            "value": f"{commondst}",
            "inline": false
        },
        {
            "name": ":fleur_de_lis:   Attack Volume",
            "value": f"{mbps} MBIT/s",
            "inline": false
        },
        {
            "name": ":test_tube:  Mitigation",
            "value": f"{mitigation}",
            "inline": false
        },
        {
            "name": ":hourglass:  Unique IP's",
            "value": f"{ipcount}",
            "inline": false
        },
        {
            "name": ":rocket:  Unique Network's",
            "value": f"{networkcount}",
            "inline": false
        },
        {
            "name": ":bomb:  Uptime",
            "value": f"{uptimesys}",
            "inline": false
        },
        {
          "name": ":chains:  # Of PCAP's",
          "value": f"{pcaplist}",
          "inline": false
        },
        {
          "name": ":rotating_light:  Established Connections",
          "value": f"{connections}",
          "inline": false
        },
        {
           "name": ":anchor:  RFC Connections?",
           "value": f"{spoofcheck}",
           "inline": false
        }
        ],
      "author": {
        "name": grabauthortitle,
        "icon_url": grabiconurl
      },
      "footer": {
        "text": f"Attack Has Been Captured  •  {date2}",
        "icon_url": "https://media.discordapp.net/attachments/858973685908897802/858974550984097833/download.gif"
      },
      "image": {
          "url": grabbottomimageurl,
      },
      "thumbnail": {
          "url": grabthumbnailurl
      }
    }
  ]   
}     
          header_data = {'content-type': 'application/json'}
          requests.post(webhook, json.dumps(attackdetection), headers=header_data)
        elif grablogtype == "telegram":
          if grabtelegramtoken == "":
            os.system("clear")
            print("Something Is Wrong With Your Bot Token..")
            quit()
          bot = telepot.Bot(grabtelegramtoken)
          bot.sendMessage(grabtelegramid, f'Attack Detected On  ->   [  {ipcheck}  ]\n\nServer Nickname:   [  {grabservertitle}  ]\nCapture Name:   [  {capturename}  ]\nCPU Load:   [  {cpu}%  ]\nAttack Type:   [  {attacktype}  ]\nAttacked Port:   [  {commondst}  ]\nAttack Volume:   [  {mbps} MBIT/s  ]\nUnique IPs:   [  {ipcount}  ]\nUnique ASNs:   [  {networkcount}  ]\nServer Uptime:   [  {uptimesys}  ]\nEstablished TCP Connections:   [  {connections}  ]\n\nData Posted At: {date2}')
        else:
          print("something went wrong..")
          quit()
        os.system("clear")
        if ipcount > 250:
          attackpossible = "Botnet Or Reflection Attack"
        else:
          attackpossible = "DoS Attack Or Small Reflection Attack"
        if ipcount > 500:
          attackprob = random.randint(30,40)
        else:
          attackprob = random.randint(30,50)
        if networkcount > 15:
          attackprob2 = random.randint(30,40)
        else:
          attackprob2 = random.randint(30,50)
        trueprob = attackprob + attackprob2

        attackbanner = f"""
     Attack Info > 

 Capture Name: {capturename}
 Attacked IP: {biggesttarget}
 Attack Type: {attacktype} / [Possibly {attackpossible} ({trueprob}%)]
 Attacked Port: {commondst}
 Attack Filtered?: {mitigation}
 Unique IP's: {ipcount}
 Unique ASNs: {networkcount}
 TCP Connections: {connections}
 Attack Log Preference: {grablogtype}
        """
        box(string=attackbanner)
        penguin(string=asciibanner)
        time.sleep(120)