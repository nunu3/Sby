# -*- ห้ามขายไฟลต่อ -*- 
import TONapi
from TONapi import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

aditmadzs = LineClient("Hack918kiss.th@gmail.com","0C122yd51411")
ki = LineClient("xfuaftsup@braun4email.com","delon513")
kk = LineClient("aakget@onecitymail.com","delon513")
kc = LineClient("uebeejbma@22office.com","delon513")
km = LineClient("xmvzkv@22office.com","delon513")
kb = LineClient("hdbjnj@22office.com","delon513")
kd = LineClient("mthjbubd@22office.com","delon513")
ke = LineClient("ksqgbqh@utooemail.com","delon513")
kf = LineClient("datffx@utooemail.com","delon513")
kg = LineClient("pjovjf@braun4email.com","delon513")
kh = LineClient("naokyqrt@onecitymail.com","delon513")
g1 = LineClient("xkmkuwje@onecitymail.com","delon513")

#aditmadzs = #LineClient(authToken="")
#ki = #LineClient(authToken="")
#kk = #LineClient(authToken="")
#kc = #LineClient(authToken="")
#km = #LineClient(authToken="")
#kb = #LineClient(authToken="")
#kd = #LineClient(authToken="")
#ke = #LineClient(authToken="")
#kf = #LineClient(authToken="")
#kg = #LineClient(authToken="")
#kh = #LineClient(authToken="")
#g1 = #LineClient(authToken="")
poll = LinePoll(aditmadzs)
call = aditmadzs
aditmadzsProfile = aditmadzs.getProfile()
creator = ["u2145c228335ffe016af96d4ba21968a8"]
owner = ["u2145c228335ffe016af96d4ba21968a8"]
admin = ["u2145c228335ffe016af96d4ba21968a8"]
staff = ["u2145c228335ffe016af96d4ba21968a8"]
mid = aditmadzs.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = kb.getProfile().mid
Fmid = kd.getProfile().mid
Gmid = ke.getProfile().mid
Hmid = kf.getProfile().mid
Imid = kg.getProfile().mid
Jmid = kh.getProfile().mid
g1MID = g1.getProfile().mid
KAC = [aditmadzs,ki,kk,kc,km,kb,kd,ke,kf,kg,kh]
ABC = [ki,kk,kc,km,kb,kd,ke,kf,kg,kh]
kicker = [ki,kk,kc,km,kb,kd,ke,kf,kg,kh]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]
Aditmadzs = admin + staff
zxcv = mid
protectqr = []
protectkick = []
protectkick1 = []
protectjoin = []
protectinvite = []
protectcancel = []
protectcanceljs = []
protectantijs = []
ghost = []
protecARoin = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = km.getProfile().displayName
responsename5 = kb.getProfile().displayName
responsename6 = kd.getProfile().displayName
responsename7 = ke.getProfile().displayName
responsename8 = kf.getProfile().displayName
responsename9 = kg.getProfile().displayName
responsename10 = kh.getProfile().displayName

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

aditProfile = aditmadzs.getProfile()
myProfile["displayName"] = aditProfile.displayName
myProfile["statusMessage"] = aditProfile.statusMessage
myProfile["pictureStatus"] = aditProfile.pictureStatus

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    
with open('protectcanceljs.json', 'r') as fp:
    protectcanceljs = json.load(fp)    
with open('protectantijs.json', 'r') as fp:
    protectantijs = json.load(fp)
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kk.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kc.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        km.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention5(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kb.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention6(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kd.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention7(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ke.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMention8(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kf.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention9(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kg.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention10(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kh.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🐚 Group : "+str(len(gid))+"\n🐚 Teman : "+str(len(teman))+"\n🐚 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🐚 Runtime : \n • "+bot
        aditmadzs.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = """╔════════════════════╗
        ผู้สร้าง : ɴᴏᴛᴀᴘʜᴀsᴇ
╠════════════════════╝
╠❂➣ Help
╠❂➣ Help bot
╠❂➣ Me
╠❂➣ Mymid
╠❂➣ Mid「@」
╠❂➣ Info 「@」
╠❂➣ Kick1 「@」
╠❂➣ bye1-0「@」
╠❂➣ คทบอท
╠❂➣ Set
╠❂➣ ข้อมุลบอท
╠❂➣ รีบอท
╠❂➣ ออน
╠❂➣ ผส
╠❂➣ เชคคิก
╠❂➣ เชคชื่อ
╠❂➣ Sp「เช็คสปีดคิก」
╠❂➣ /Sp「เช็คสปีดเชล」
╠❂➣ แทค
╠❂➣ มา
╠❂➣ ไป
╠❂➣ k1「1-10คิกมาทีละตัว」
╠❂➣ kแจก「คิกส่งของขวัณ」
╠❂➣ แจก「หลักส่งของขวั๋」
╠❂➣ Ginfo
╠❂➣ เปิดลิ้ง
╠❂➣ ปิดลิ้ง
╠❂➣ ลิ้ง
╠❂➣ ทดสอบ [ คำสั่งบินห้อง ]
╠❂➣ กลุ่มบอท
╠❂➣ กลุ่มคิก1「ใส่1-10คือชื่อคิก」
╠❂➣ เพื่อน
╠❂➣ Infogrup「angka」
╠❂➣ Infomem「angka」
╠❂➣ อ่าน「เปิด/ปิด」
╠❂➣ อ่าน
╠❂➣ จับคนยืน「เปิด/ปิด」
╠❂➣ ประกาศ:「ใสข้อความ」
╠❂➣ Setkey「New Key」
╠❂➣ Mykey
╠❂➣ Resetkey
╠═════❦ การป้องกัน ❦═══════
╠❂➣ กันทั้งหมด「เปิด/ปิด」
╠❂➣ กันลิ้ง「เปิด/ปิด」
╠❂➣ กันเตะ「เปิด/ปิด」
╠❂➣ กันยกเชิญ「เปิด/ปิด」
╠❂➣ กันเข้า「เปิด/ปิด」
╠❂➣ กันเชิญ「เปิด/ปิด」
╠❂➣ ป้องกันบอทบิน「เปิด/ปิด」
╠❂➣ ป้องกันบอทบิน
╠❂➣ ป้องกันยกเชิญบอท「เปิด/ปิด」
╠❂➣ ผี「เปิด/ปิด」
╠❂➣ ผีกัน「เปิด/ปิด」
╠═════❦ การตั้งค่า ❦════════
╠❂➣ เชล「ปิด/เปิด」
╠❂➣ เตะแทค「เปิด/ปิด」
╠❂➣ อ่านตัส「เปิด/ปิด」
╠❂➣ ตอบแทค「เปิด/ปิด」
╠❂➣ ส่งกิ๊ฟ「เปิด/ปิด」
╠❂➣ เข้ากลุ่ม「เปิด/ปิด」
╠❂➣ ออกแชท「เปิด/ปิด」
╠❂➣ บล็อค「เปิด/ปิด」
╠❂➣ ต้อนรับ「เปิด/ปิด」
╠❂➣ Simi「on/off」
╠❂➣ มุดลิ้ง「เปิด/ปิด」
╠❂➣ Listbot
╠════════════════════╗
◄]·✪http://line.me/ti/p/%40scj2592u✪·[►
╚════════════════════╝"""
    return helpMessage
    
    

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = """╔════════════════════╗
             ผู้สร้าง : ɴᴏᴛᴀᴘʜᴀsᴇ
╠════════════════════╝
╠❂➣ เชคออก
╠❂➣ Cek spam
╠❂➣ Cek pesan
╠❂➣ เชคแทค
╠❂➣ เชคเข้า
╠❂➣ ตั้งแทค:「ใสข้อความ」
╠❂➣ Set spam:「Text」
╠❂➣ Set pesan:「Text」
╠❂➣ ตั้งทักคนยืน「ใสข้อความ」
╠❂➣ ตั้งต้อนรับ「ใสข้อความ」
╠❂➣ ตั้งออก:「ใสข้อความ」
╠❂➣ Myname:「Nama」
╠❂➣ Bot1name:「เปลี่ยนชื่อ1-10」
╠❂➣ Bot1up「เปลียนดิส1-10」
╠❂➣ Updatefoto
╠❂➣ Updategrup
╠❂➣ Updatebot
╠❂➣ Setkey「New Key」
╠❂➣ Mykey
╠❂➣ Resetkey
╠❂➣ ลบแชท「ลบแชทเชล」
╠❂➣ ลบแชท คิก
╠❂➣ Leave:「ใส่ชื่อกลุ่ม」
╠══════❦ บัญชีดำ ❦═══════
╠❂➣ คทดำ
╠❂➣ ดำ:เปิด
╠❂➣ ขาว:เปิด
╠❂➣ ดำ「@」
╠❂➣ ขาว「@」
╠❂➣ Talkban「@」
╠❂➣ Untalkban「@」
╠❂➣ Talkban:on
╠❂➣ Untalkban:on
╠❂➣ เชคดำ
╠❂➣ Talkbanlist
╠❂➣ cb
╠❂➣ รีข้อมุล「เปิดดำ/ขาว=แล้วลงคำนี้ปิด」
╠════════════════════╗
◄]·http://line.me/ti/p/%40scj2592u·[►
╚════════════════════╝"""
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            aditmadzs.reissueGroupTicket(op.param1)
                            X = aditmadzs.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            aditmadzs.updateGroup(X)
                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                   wait["blacklist"][op.param2] = True
                   random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                   random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        aditmadzs.sendMessage(op.param1, wait["message"])
                        aditmadzs.blockContact(op.param1)       
#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
        if op.type == 19:
            if op.param1 in protectkick1:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        g1.acceptGroupInvitation(op.param1)
                        g1.kickoutFromGroup(op.param1,[op.param2])	
                        g1.sendMessage(op.param1," เตะเขาทำควยรัย (｀・ω・´)")						
                        G = g1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        g1.updateGroup(G)
                        Ticket = g1.reissueGroupTicket(op.param1)
                        aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)							
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                        km.acceptGroupInvitationByTicket(op.param1,Ticket)	
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)						
                        G.preventedJoinByTicket = True
                        g1.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        g1.leaveGroup(op.param1)
                        aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                else:
                    pass
							
						
                if op.param3 in g1MID:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        aditmadzs.findAndAddContactsByMid(op.param3)
                        aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                        aditmadzs.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        aditmadzs.findAndAddContactsByMid(op.param3)
                        aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                        aditmadzs.sendMessage(op.param1,"=AntiJS Invited=")
                        
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = aditmadzs.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        aditmadzs.updateGroup(G)
                        invsend = 0
                        Ticket = aditmadzs.reissueGroupTicket(op.param1)
                        g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        g1.kickoutFromGroup(op.param1,[op.param2])
                        g1.leaveGroup(op.param1)
                        X = aditmadzs.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        aditmadzs.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            g1.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        pass
                                    
        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)
                            g1.inviteIntoGroup(op.param1,[mid])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            aditmadzs.inviteIntoGroup(op.param1,[g1MID])
                        except:
                            pass              
        if op.type == 32:
            if op.param1 in protectcanceljs:
                if op.param3 in Bots:    
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                aditmadzs.inviteIntoGroup(op.param1,[g1MID])		
                                G.preventedJoinByTicket = True
                                random.choice(ABC).updateGroup(G)
                        except:
                            pass
                    return  
#===========Cancel============#

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.findAndAddContactsByMid(op.param1,[Zmid])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                aditmadzs.findAndAddContactsByMid(op.param1,[Zmid])
                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                aditmadzs.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass
                return

#-------------------------------------------------------------------------------      

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        aditmadzs.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            aditmadzs.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                aditmadzs.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        aditmadzs.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            aditmadzs.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                km.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                            km.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        km.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = km.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    km.updateGroup(G)
                                    Ticket = km.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = km.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    km.updateGroup(G)
                                    Ticket = km.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            km.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kd.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.updateGroup(G)
                                    Ticket = kd.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kd.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kd.updateGroup(G)
                                    Ticket = kd.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kf.kickoutFromGroup(op.param1,[op.param2])
                            kf.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kg.kickoutFromGroup(op.param1,[op.param2])
                                kg.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ke.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ke.updateGroup(G)
                                    Ticket = ke.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kg.kickoutFromGroup(op.param1,[op.param2])
                            kg.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kh.kickoutFromGroup(op.param1,[op.param2])
                                kh.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kf.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.updateGroup(G)
                                    Ticket = kf.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kf.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kf.updateGroup(G)
                                    Ticket = kf.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        kg.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kg.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                    kg.updateGroup(G)
                                    Ticket = kg.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kg.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kg.updateGroup(G)
                                    Ticket = kg.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kf.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kh.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kh.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                    kh.updateGroup(G)
                                    Ticket = kh.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kh.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kh.updateGroup(G)
                                    Ticket = kh.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            kg.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kh.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kh.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kh.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = aditmadzs.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    aditmadzs.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kh.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            kh.acceptGroupInvitation(op.param1)
                                        except:
                                            pass

                return
        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass                

        if op.type == 55:
            try:
                if op.param1 in Setmain["ADITMADZSreadPoint"]:
                   if op.param2 in Setmain["ADITMADZSreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ADITMADZSreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = aditmadzs.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               aditmadzs.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           aditmadzs.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                    

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, wait["Respontag"])
                           aditmadzs.sendMessage(msg.to, None, contentMetadata={"STKID":"21715710","STKPKGID":"9662","STKVER":"2"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           aditmadzs.sendMessage(msg.to, "Yang suka ngetag minta di gift yaa!?\nCek di chat, udah aku gift tuh...")
                           aditmadzs.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, "Jangan tag saya....")
                           aditmadzs.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"「Cek ID Sticker」\n🐚 STKID : " + msg.contentMetadata["STKID"] + "\n⏩ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n⏩ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"⏩ Nama : " + msg.contentMetadata["displayName"] + "\n⏩ MID : " + msg.contentMetadata["mid"] + "\n⏩ Status : " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"⏩ Nama : " + msg.contentMetadata["displayName"] + "\n⏩ MID : " + msg.contentMetadata["mid"] + "\n⏩ Status : " + contact.statusMessage + "\n⏩ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        aditmadzs.sendMessage(msg.to,"เพิ่มลงในบัญชีดำแล้ว")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"เพิ่มลงในบัญชีดำแล้ว")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"ลบออกจากบัญชีดำแล้ว")
                    else:
                        wait["dblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"ลบออกจากบัญชีดำแล้ว")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        aditmadzs.sendMessage(msg.to,"รายชื่อู้ติดต่อนี้อยู่ใน Talkblacklist แล้ว")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"เพิ่มลงในบัญชีดำแล้ว")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"รายชื่อู้ติดต่อนี้ไม่อยู่ใน Talkblacklist")
                    else:
                        wait["Talkdblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"ลบออกจากบัญชีดำแล้ว")

#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ADITMADZSfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ADITMADZSfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif Bmid in Setmain["ADITMADZSfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif Cmid in Setmain["ADITMADZSfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")
                        elif Dmid in Setmain["ADITMADZSfoto"]:
                            path = km.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Dmid]
                            km.updateProfilePicture(path)
                            km.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	
                        elif Emid in Setmain["ADITMADZSfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Emid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")								
                        elif Fmid in Setmain["ADITMADZSfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Fmid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	
                        elif Gmid in Setmain["ADITMADZSfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Gmid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	
                        elif Hmid in Setmain["ADITMADZSfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Hmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	
                        elif Imid in Setmain["ADITMADZSfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Imid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	
                        elif Jmid in Setmain["ADITMADZSfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Jmid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	
                        elif g1MID in Setmain["ADITMADZSfoto"]:
                            path = g1.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][g1MID]
                            g1.updateProfilePicture(path)
                            g1.sendMessage(msg.to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")	

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)	
                     path4 = km.downloadObjectMsg(msg_id)
                     path5 = kb.downloadObjectMsg(msg_id)	
                     path6 = kd.downloadObjectMsg(msg_id)
                     path7 = ke.downloadObjectMsg(msg_id)
                     path8 = kf.downloadObjectMsg(msg_id)
                     path9 = kg.downloadObjectMsg(msg_id)
                     path10 = kh.downloadObjectMsg(msg_id)
                     path11 = g1.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, ">OK<")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, ">OK<")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, ">OK<")	
                     km.updateProfilePicture(path4)
                     km.sendMessage(msg.to, ">OK<")	
                     kb.updateProfilePicture(path5)
                     kb.sendMessage(msg.to, ">OK<")
                     kd.updateProfilePicture(path6)
                     kd.sendMessage(msg.to, ">OK<")	
                     ke.updateProfilePicture(path7)
                     ke.sendMessage(msg.to, ">OK<")	
                     kf.updateProfilePicture(path8)
                     kf.sendMessage(msg.to, ">OK<")	
                     kg.updateProfilePicture(path9)
                     kg.sendMessage(msg.to, ">OK<")	
                     kh.updateProfilePicture(path10)
                     kh.sendMessage(msg.to, ">OK<")	
                     g1.updateProfilePicture(path11)
                     g1.sendMessage(msg.to, ">OK<")	
               if msg.contentType == 0:
                    if wait["autoRead"] == True:                        
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        km.sendChatChecked(msg.to, msg_id)
                        kb.sendChatChecked(msg.to, msg_id)						
                        kd.sendChatChecked(to, msg_id)
                        ke.sendChatChecked(to, msg_id)
                        kf.sendChatChecked(to, msg_id)
                        kg.sendChatChecked(to, msg_id)
                        kh.sendChatChecked(to, msg_id)
                        g1.sendChatChecked(to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               aditmadzs.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "เชล เปิด":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "ปิดเชลเรียบร้อย...")
                                
                        elif cmd == "เชล ปิด":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "เปิดเชลเรียบร้อย...")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               aditmadzs.sendMessage(msg.to, str(helpMessage1))

                        if cmd == "จับลบข้อความ เปิด":
                            if msg._from in admin:
                                wait["unsend"] = True
                                aditmadzs.sendMessage(msg.to, "เปิดจับคนลบข้อความเรียบร้อย...")
                                
                        if cmd == "จับลบข้อความ ปิด":
                            if msg._from in admin:
                                wait["unsend"] = False
                                aditmadzs.sendMessage(msg.to, "ปิดจับคนลบข้อความเรียบร้อย")             
                        elif cmd == "เชคคิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sendMention1(msg.to, sender, "➸  ", "")
                                sendMention2(msg.to, sender, "➸  ", "")
                                sendMention3(msg.to, sender, "➸  ", "")
                                sendMention4(msg.to, sender, "➸  ", "")
                                sendMention5(msg.to, sender, "➸  ", "")
                                sendMention6(msg.to, sender, "➸  ", "")
                                sendMention7(msg.to, sender, "➸  ", "")
                                sendMention8(msg.to, sender, "➸  ", "")
                                sendMention9(msg.to, sender, "➸  ", "")
                                sendMention10(msg.to, sender, "➸  ", "")
                        elif cmd == "kแจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kk.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kc.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                km.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kd.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kb.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                ke.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kf.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kg.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                                kh.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "1แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "2แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kk.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "3แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                km.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "4แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kd.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "5แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kb.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "6แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ke.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "7แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kf.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "8แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kg.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "9แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kf.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "10แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                kh.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "แจก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                aditmadzs.sendMessage(to, text=None, contentMetadata=None, contentType=9)                   

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ┏━━━━━━━━━━━━━━━━━\n┃          การตั้งค่า\n┣━━━━━━━━━━━━━━━━━━━━\n"
                                if wait["sticker"] == True: md+="┃ ✔️ Sticker「ON」\n"
                                else: md+="┃ ✖ Sticker「OFF」\n"
                                if wait["contact"] == True: md+="┃ ✔️ Contact「ON」\n"
                                else: md+="┃ ✖ Contact「OFF」\n"
                                if wait["talkban"] == True: md+="┃ ✔️ Talkban「ON」\n"
                                else: md+="┃ ✖ Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃ ✔️ Notag「ON」\n"
                                else: md+="┃ ✖ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="┃ ✔️ Respon「ON」\n"
                                else: md+="┃ ✖ Respon「OFF」\n"
                                if wait["Mentiongift"] == True: md+="┃ ✔️ Respongift「ON」\n"
                                else: md+="┃ ✖ Respongift「OFF」\n"                                
                                if wait["autoJoin"] == True: md+="┃ ✔️ Autojoin「ON」\n"
                                else: md+="┃ ✖ Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="┃ ✔️ Jointicket「ON」\n"
                                else: md+="┃ ✖ Jointicket「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="┃ ✔️ Autoadd「ON」\n"
                                else: md+="┃ ✖ Autoadd「OFF」\n"
                                if msg.to in welcome: md+="┃ง┃ ✔️ Welcome「ON」\n"
                                else: md+="┃ ✖ Welcome「OFF」\n"
                                if msg.to in simisimi: md+="┃ ✔️ Simisimi「ON」\n"
                                else: md+="┃ ✖ Simisimi「OFF」\n"                                
                                if wait["autoLeave"] == True: md+="┃ ✔️ Autoleave「ON」\n"
                                else: md+="┃ ✖ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃ ✔️ Protecturl「ON」\n"
                                else: md+="┃ ✖ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃ ✔️ Protectjoin「ON」\n"
                                else: md+="┃ ✖ Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="┃ ✔️ Protectkick「ON」\n"
                                else: md+="┃ ✖ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃ ✔️ Protectcancel「ON」\n"
                                else: md+="┃ ✖ Protectcancel「OFF」\n"
                                if msg.to in protectinvite: md+="┃ ✔️ Protectinvite「ON」\n"
                                else: md+="┃ ✖ Protectinvite「OFF」\n"  
                                if msg.to in protectcanceljs: md+="┃ ✔️ Protectantijs「ON」\n"
                                else: md+="┃ ✖ protectantijs「OFF」\n"
                                if msg.to in protectantijs: md+="┃ ✔️ protectcanceljs「ON」\n"
                                else: md+="┃ ✖ Protectcanceljs「OFF」\n"
                                if msg.to in ghost: md+="┃ ✔️ ghost「ON」\n"
                                else: md+="┃ ✖ ghost「OFF」\n"                                                
                                aditmadzs.sendMessage(msg.to, md+"┣━━━━━━━━━━━━━━━━━━━━\n┃✪ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃✪ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ┗━━━━━━━━━━━━━━━━━")

                        elif cmd == "creator" or text.lower() == 'ผส':
                            if msg._from in admin:
                                aditmadzs.sendMessage(msg.to,"ผู้สร้างบอท...") 
                                ma = ""
                                for i in creator:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "ข้อมุลบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 TON SelfBOT 1 Assist 」\n")
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "คท" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               aditmadzs.sendMessage1(msg)

                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "ชื่อ : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                        elif text.lower() == "ทดสอบ":
                            if msg._from in admin:
                                gs = ki.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for b in Bots:
                                    if b in targets:
                                        try:
                                            targets.remove(b)
                                        except:
                                            pass
                                aditmadzs.sendText(msg.to,"== ▒▒▒▓▓▓「SEFT By. ŋีஆএণथஆึსஆัюℓઈ❍ะ」\n\nผู้สร้าง : line.me/ti/p/%40scj2592u")
                                for target in targets:
                                    try:
                                        klist = [ki,kk,kc,km,kb,kd,ke,kf,kg,kh]
                                        kicker = random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                    except:
                                        pass 

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "❧ Nama : "+str(mi.displayName)+"\n🐚 Mid : " +key1+"\n🐚 Status : "+str(mi.statusMessage))
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                                   aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd.startswith("ประกาศ: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = aditmadzs.getGroupIdsJoined()
                               for group in saya:
                                   aditmadzs.sendMessage(group,"=======[✪ɴᴏᴛᴀᴘʜᴀsᴇ✪]=======\n\n"+pesan+"\n\nCreator : line.me/ti/p/%40scj2592u")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "รีบอท":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               aditmadzs.sendMessage(msg.to, "โปรดรอ 5 นาที่บอทกำลังเข้าระบบใหม่อีกครั้ง...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "บอททำงานมาแล้ว " +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendMessage(msg.to, "❧ BOT Grup Info\n\n ❧ Nama Group : {}".format(G.name)+ "\n🐚 ID Group : {}".format(G.id)+ "\n🐚 Pembuat : {}".format(G.creator.displayName)+ "\n🐚 Waktu Dibuat : {}".format(str(timeCreated))+ "\n🐚 Jumlah Member : {}".format(str(len(G.members)))+ "\n🐚 Jumlah Pending : {}".format(gPending)+ "\n🐚 Group Qr : {}".format(gQr)+ "\n🐚 Group Ticket : {}".format(gTicket))
                                aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "⏩ BOT Grup Info\n"
                                ret_ += "\n⏩ Name : {}".format(G.name)
                                ret_ += "\n⏩ ID : {}".format(G.id)
                                ret_ += "\n⏩ Creator : {}".format(gCreator)
                                ret_ += "\n⏩ Created Time : {}".format(str(timeCreated))
                                ret_ += "\n⏩ Member : {}".format(str(len(G.members)))
                                ret_ += "\n⏩ Pending : {}".format(gPending)
                                ret_ += "\n⏩ Qr : {}".format(gQr)
                                ret_ += "\n⏩ Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "⏩ "+ str(no) + ". " + mem.displayName
                                aditmadzs.sendMessage(to,"⏩ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = aditmadzs.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)

                        elif cmd == "เพื่อน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getAllContactIds()
                               for i in gid:
                                   G = aditmadzs.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               aditmadzs.sendMessage(msg.to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "กลุ่มบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "กลุ่มคิก1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = km.getGroupIdsJoined()
                               for i in gid:
                                   G = km.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               km.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก5":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kd.getGroupIdsJoined()
                               for i in gid:
                                   G = kd.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kd.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก6":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก7":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก8":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kf.getGroupIdsJoined()
                               for i in gid:
                                   G = kf.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kf.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก9":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kg.getGroupIdsJoined()
                               for i in gid:
                                   G = kg.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kg.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "กลุ่มคิก10":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kh.getGroupIdsJoined()
                               for i in gid:
                                   G = kh.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.name+ "\n"
                               kh.sendMessage(msg.to,"┏━━[ GROUP LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ จำนวน「"+str(len(gid))+"」Groups ]")
                        elif cmd == "เปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "เปิดลิ้งกลุ่มเรียบร้อย...")

                        elif cmd == "ปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = ki.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ki.updateGroup(X)
                                   ki.sendMessage(msg.to, "ปิดลิ้งกลุ่มเรียบร้อย...")

                        elif cmd == "ลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = ki.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ki.updateGroup(x)
                                   gurl = ki.reissueGroupTicket(msg.to)
                                   ki.sendMessage(msg.to, "ชื่อกลุ่ม : "+str(x.name)+ "\nลิ้งกลุ่ม : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                aditmadzs.sendMessage(msg.to,"โปรดส่งรูปลงมา.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                ki.sendMessage(msg.to,"โปรดส่งรูปลงมา.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][mid] = True
                                aditmadzs.sendMessage(msg.to,"โปรดส่งรูปลงมา.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Amid] = True
                                ki.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})

                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})

                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Dmid] = True
                                km.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Emid] = True
                                kb.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Fmid] = True
                                kd.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot7up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Gmid] = True
                                ke.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot8up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Hmid] = True
                                kf.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot9up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Imid] = True
                                kg.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Jmid] = True
                                kh.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd == "bot11up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][g1MID] = True
                                g1.sendMessage(msg.to,"กรุณาส่งภาพด้วย.....", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
								
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                aditmadzs.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                km.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                kh.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
								
                        elif cmd.startswith("botkickname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = g1.getProfile()
                                profile.displayName = string
                                g1.updateProfile(profile)
                                g1.sendMessage(msg.to,"เปลี่ยนชื่อเป็น " + string + "")
                        elif cmd == "เพิ่ม":
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    clfr = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]
                                    kkfr = [mid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]#ki=Amid
                                    aafr = [mid,Amid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]#kk=Bmid
                                    abfr = [mid,Amid,Bmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]#kc=Cmid
                                    acfr = [mid,Amid,Bmid,Cmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]#km=Dmid
                                    adfr = [mid,Amid,Bmid,Cmid,Dmid,Fmid,Gmid,Hmid,Imid,Jmid,g1MID]#kb=Emid
                                    aefr = [mid,Amid,Bmid,Cmid,Dmid,Emid,Gmid,Hmid,Imid,Jmid,g1MID]#kd=Fmid
                                    affr = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Hmid,Imid,Jmid,g1MID]#ke=Gmid
                                    agfr = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Imid,Jmid,g1MID]#kf=Hmid
                                    ahfr = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Jmid,g1MID]#kg=Imid
                                    aifr = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,g1MID]#kh=Jmid
                                    ajfr = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]#g1=g1mid
                                    for addcl in clfr:
                                        aditmadzs.findAndAddContactsByMid(addcl)
                                    aditmadzs.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addki in kkfr:
                                        ki.findAndAddContactsByMid(addki)
                                    ki.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkk in aafr:
                                        kk.findAndAddContactsByMid(addkk)
                                    kk.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkc in abfr:
                                        kc.findAndAddContactsByMid(addkc)
                                    kc.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkm in acfr:
                                        km.findAndAddContactsByMid(addkm)
                                    km.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://http://line.me/ti/p/%40scj2592u'})
                                    for addkb in adfr:
                                        kb.findAndAddContactsByMid(addkb)
                                    kb.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkd in aefr:
                                        kd.findAndAddContactsByMid(addkd)
                                    kd.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addke in affr:
                                        ke.findAndAddContactsByMid(addke)
                                    ke.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkf in agfr:
                                        kf.findAndAddContactsByMid(addkf)
                                    kf.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkg in ahfr:
                                        kg.findAndAddContactsByMid(addkg)
                                    kg.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addkh in aifr:
                                        kh.findAndAddContactsByMid(addkh)
                                    kh.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})
                                    for addg1 in ajfr:
                                        g1.findAndAddContactsByMid(addg1)
                                    g1.sendMessage(to,"👼แอดเพื่อนเรียบร้อย👼", contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'Creator', 'AGENT_LINK': 'http://line.me/ti/p/%40scj2592u'})


                        elif cmd == "คทบอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               aditmadzs.sendMessage1(msg)							   
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               aditmadzs.sendMessage1(msg)	
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': g1MID}
                               aditmadzs.sendMessage1(msg)	

                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   aditmadzs.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "ลบแชท คิก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   ki.sendMessage(msg.to,"คิก1 ลบแชทเรียบร้อย...")
                                   kk.removeAllMessages(op.param2)
                                   kk.sendMessage(msg.to,"คิก2 ลบแชทเรียบร้อย...")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"คิก3 ลบแชทเรียบร้อย...")
                                   km.removeAllMessages(op.param2)
                                   km.sendMessage(msg.to,"คิก4 ลบแชทเรียบร้อย...")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"คิก5 ลบแชทเรียบร้อย...")
                                   kd.removeAllMessages(op.param2)	
                                   kd.sendMessage(msg.to,"คิก6 ลบแชทเรียบร้อย...")
                                   ke.removeAllMessages(op.param2)	
                                   ke.sendMessage(msg.to,"คิก7 ลบแชทเรียบร้อย...")
                                   kf.removeAllMessages(op.param2)	
                                   kf.sendMessage(msg.to,"คิก8 ลบแชทเรียบร้อย...")
                                   kg.removeAllMessages(op.param2)	
                                   kg.sendMessage(msg.to,"คิก9 ลบแชทเรียบร้อย...")
                                   kh.removeAllMessages(op.param2)	
                                   kh.sendMessage(msg.to,"คิก10 ลบแชทเรียบร้อย...")
                                   g1.removeAllMessages(op.param2)	
                                   aditmadzs.sendMessage(msg.to,"ลบแชทเรียบร้อยแล้วลูกพี่..")
                               except:
                                   pass
#===========BOT UPDATE============#
                        elif msg.text.lower().startswith("แทค"):
                          if msg._from in admin:						
                            data = msg.text[len("แทค"):].strip()
                            if data == "":
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == "<":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count > mentargs:
                                                break
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == ">":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                if mentargs >= 0:
                                    strt = len(str(mentargs)) + 2
                                else:
                                    strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count < mentargs:
                                                count += 1
                                                continue
                                    akh = akh + len(str(count)) + 2 + 5
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                            elif data[0] == "=":
                                mentargs = int(data[1:].strip())
                                group = aditmadzs.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members if contact.mid != zxcv]
                                cb = ""
                                cb2 = ""
                                count = 1
                                akh = int(0)
                                cnt = 0
                                for md in nama:
                                    if count != mentargs:
                                                count += 1
                                                continue
                                    akh = akh + len(str(count)) + 2 + 5
                                    strt = len(str(count)) + 2
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + len(str(count+1)) + 2 + 6
                                    akh = akh + 1
                                    cb2 += str(count)+". @name\n"
                                    cnt = cnt + 1
                                    if cnt == 20:
                                                cb = (cb[:int(len(cb)-1)])
                                                cb2 = cb2[:-1]
                                                msg.contentType = 0
                                                msg.text = cb2
                                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                                try:
                                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                                except:
                                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
                                                cb = ""
                                                cb2 = ""
                                                strt = len(str(count)) + 2
                                                akh = int(0)
                                                cnt = 0
                                    count += 1
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    aditmadzs.sendMessage(msg.to,text = cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)
                                except:
                                    aditmadzs.sendText(msg.to,"[[NO MENTION]]")
#===========BOT UPDATE============#
#===========BOT UPDATE============#
#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                               group = aditmadzs.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ BOT\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))
#===========BOT UPDATE============#
                        elif cmd == "เชคชื่อ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kk.sendMessage(msg.to,responsename2, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kc.sendMessage(msg.to,responsename3, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kb.sendMessage(msg.to,responsename4, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                km.sendMessage(msg.to,responsename5, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kd.sendMessage(msg.to,responsename6, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                ke.sendMessage(msg.to,responsename7, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kf.sendMessage(msg.to,responsename8, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kg.sendMessage(msg.to,responsename9, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})
                                kh.sendMessage(msg.to,responsename10, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+aditmadzs.getContact(mid).pictureStatus, 'AGENT_NAME': 'CheckBot', 'AGENT_LINK': 'http://line.me/ti/p/~jamerockzaza'})								

                        elif cmd == "เชิญผี":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
                                    aditmadzs.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    km.acceptGroupInvitation(msg.to)								
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kh.acceptGroupInvitation(msg.to)									
                                except:
                                    pass
                                
                        elif cmd == "ป้องกันบอทบิน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = aditmadzs.getGroup(msg.to)
                                    aditmadzs.inviteIntoGroup(msg.to, [g1MID])
                                    aditmadzs.sendMessage(msg.to,"กลุ่ม 「"+str(ginfo.name)+"」 โปรดสั่ง  ป้องกันบอทบิน เปิด ")
                                except:
                                    pass
    
                        elif cmd == "มา":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)	
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)									
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)
                        elif cmd == "คิกออกหมด":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kb.leaveGroup(i)								
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)


                        elif cmd == "ไป":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)								
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                        elif cmd == "บอทออก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                aditmadzs.sendMessage(msg.to, "บายๆๆ "+str(G.name))
                                aditmadzs.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)								
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                        elif cmd == "ผมออก":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                aditmadzs.leaveGroup(msg.to)

                        elif cmd.startswith("kออก "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = aditmadzs.getGroupIdsJoined()
                                for i in gid:
                                    h = aditmadzs.getGroup(i).name
                                    if h == ng:
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        km.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        kg.leaveGroup(i)
                                        kh.leaveGroup(i)							
                                        aditmadzs.sendMessage(to,"ออกจากกลุ่มเรียบร้อยแล้ว " +h)

                        elif cmd == "k1":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "k2":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "k3":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "k4":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = km.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                km.updateGroup(G)

                        elif cmd == "k5":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "k6":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "k7":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "k8":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kf.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)

                        elif cmd == "k9":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)

                        elif cmd == "k10":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)
								
                        elif cmd == "ผีมา":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = g1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                g1.updateGroup(G)

                        elif cmd == "ผีออก":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                g1.leaveGroup(msg.to)

                        elif cmd == "speed" or cmd == "/sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               aditmadzs.sendMessage("u377efb183a65535b0152ebf3555723f8", '.')
                               elapsed_time = time.time() - start
                               aditmadzs.sendMessage(msg.to, "%s เเรงแล้วลูกพี่" % (elapsed_time))


                        elif cmd == "speedbot" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start1 = time.time()
                               ki.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start1
                               ki.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start2 = time.time()
                               kk.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start2
                               kk.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start3 = time.time()
                               kc.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start3
                               kc.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start4 = time.time()
                               km.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start4
                               km.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start5 = time.time()
                               kd.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start5
                               kd.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start6 = time.time()
                               kb.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start6
                               kb.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start7 = time.time()
                               ke.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start7
                               ke.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start8 = time.time()
                               kf.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start8
                               kf.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))
                               start9 = time.time()
                               kg.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start9
                               kg.sendMessage(msg.to, "%s เร็วมากพอแล้ว" % (elapsed_time))
                               start10 = time.time()
                               kh.sendMessage("u21d04f683a70ee8776c4c58a0358c204", '.')
                               elapsed_time = time.time() - start10
                               kh.sendMessage(msg.to, "%s เร็วมากพอแล้ว " % (elapsed_time))

                        elif cmd == "อ่าน เปิด":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ADITMADZSreadPoint'][msg.to] = msg_id
                                 Setmain['ADITMADZSreadMember'][msg.to] = {}
                                 aditmadzs.sendMessage(msg.to, "ตั้งเวลาจับคนอ่านเรียบร้อย ผิม อ่าน\n\n : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "อ่าน ปิด":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ADITMADZSreadPoint'][msg.to]
                                 del Setmain['ADITMADZSreadMember'][msg.to]
                                 aditmadzs.sendMessage(msg.to, "ปิดเวลาจับคนอ่านเรียบร้อย\n\n : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "อ่าน":
                          if msg._from in admin:
                            if msg.to in Setmain['ADITMADZSreadPoint']:
                                if Setmain['ADITMADZSreadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['ADITMADZSreadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ADITMADZSreadPoint'][msg.to]
                                        del Setmain['ADITMADZSreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ADITMADZSreadPoint'][msg.to] = msg.id
                                    Setmain['ADITMADZSreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "User kosong...")
                            else:
                                aditmadzs.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "จับคนยืน เปิด":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  aditmadzs.sendMessage(msg.to, "เปิดจับคนยืนเรียบร้อย...\n\n : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "จับคนยืน ปิด":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  aditmadzs.sendMessage(msg.to, "ปิดจับคนยืนเรียบร้อย...\n\n : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  aditmadzs.sendMessage(msg.to, "โปรดเปิดจับคนยืนก่อน...")

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = ki.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  ki.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = ki.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    ki.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs) 
                                    
                        elif 'ต้อนรับ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ต้อนรับ ','')
                              if spl == 'เปิด':
                                  if msg.to in welcome:
                                       msgs = "เปิดต้อนรับเรียบร้อย..."
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดต้อนรับเรียบร้อย...\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดต้อนรับเรียบร้อย...\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดต้อนรับเรียบร้อย..."
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'กันลิ้ง ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('กันลิ้ง ','')
                              if spl == 'เปิดป้องกันลิ้งเรียบร้อย...':
                                  if msg.to in protectqr:
                                       msgs = "เปิดป้องกันลิ้งเรียบร้อย..."
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องกันลิ้งเรียบร้อย\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันลิ้งเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดป้องกันลิ้งเรียบร้อย..."
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)

                        elif 'กันเตะ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('กันเตะ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectkick:
                                       msgs = "เปิดป้องกันคนเตะกันเรียบร้อย..."
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องกันคนเตะกัน\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันเตะเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดป้องกันเตะเรียบร้อย..."
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                        elif 'ผีกัน ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ผีกัน ','')
                              if spl == 'เปิด':
                                  if msg.to in protectkick1:
                                       msgs = "เปิดป้องกันคนเตะกันด้วยผีเรียบร้อย..."
                                  else:
                                       protectkick1.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องกันคนเตะกันด้วยผีเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectkick1:
                                         protectkick1.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันด้วยผีเตะเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดป้องกันด้วยผีเตะเรียบร้อย..."
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)

                        elif 'กันเข้า ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('กันเข้า ','')
                              if spl == 'เปิด':
                                  if msg.to in protectjoin:
                                       msgs = "เปิดป้องกันคนเข้าห้องเรียบร้อย"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องกันคนเข้าห้องเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันคนเข้าห้องเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดป้องกันคนเข้าห้องเรียบร้อย"
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)

                        elif 'กันยกเชิญ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('กันยกเชิญ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectcancel:
                                       msgs = "เปิดป้องกันคนยกเลิกค้างเชิญเรียบร้อย..."
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องกันคนยกเลิกค้างเชิญเรียบร้อย...\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันคนยกเลิกค้างเชิญเรียบร้อย...\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดป้องกันคนยกเลิกค้างเชิญเรียบร้อย..."
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                                    
                        elif 'กันเชิญ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('กันเชิญ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectinvite:
                                       msgs = "เปิดป้องเชิญเรียบร้อย"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "เปิดป้องเชิญเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องเชิญเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         msgs = "ปิดป้องเชิญเรียบร้อยf"
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)        
                        elif 'ป้องกันบอทบิน ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันบอทบิน ','')
                              if spl == 'เปิด':
                                  if msg.to in protectantijs:
                                       msgs = "ป้องกันJSถูกเปิดใช้งายอยู่แล้ว"
                                  else:
                                       protectantijs[msg.to] = True
                                       f=codecs.open('protectantijs.json','w','utf-8')
                                       json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "ป้องกันJSเปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectantijs:
                                         del protectantijs[msg.to]
                                         f=codecs.open('protectantijs.json','w','utf-8')
                                         json.dump(protectantijs, f, sort_keys=True, indent=4,ensure_ascii=False)												 
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ป้องกันJSปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันJSถูกปิดใช้งายอยู่แล้ว"
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                                    
                        elif 'คิกผี ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('คิกผี ','')
                              if spl == 'เปิด':
                                  if msg.to in ghost:
                                       msgs = "คิกผีถูกเปิดใช้งานอยู่แล้ว"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "โหมดป้องกันห้องด้วยคิกผีถูกเปิดใช้งาน\nIn กลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOTPROTECT GHOST」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "โหมดป้องกันห้องด้วยคิกผีถูกปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "คิกผีถูกปิดใช้งานอยู่แล้ว"
                                    aditmadzs.sendMessage(msg.to, "「TON BOT PROTECT GHOST\n" + msgs)      
                        elif 'ป้องกันยกเชิญบอท ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ป้องกันยกเชิญบอท ','')
                              if spl == 'เปิด':
                                  if msg.to in protectcanceljs:
                                       msgs = "ป้องกันยกเลิกเชิญบอทเปิดใช้งาน"
                                  else:
                                       protectcanceljs[msg.to] = True
                                       f=codecs.open('protectcanceljs.json','w','utf-8')
                                       json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)									   
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "ป้องกันยกเลิกเชิญบอทเปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectcanceljs:
                                         del protectcanceljs[msg.to]
                                         f=codecs.open('protectcanceljs.json','w','utf-8')
                                         json.dump(protectcanceljs, f, sort_keys=True, indent=4,ensure_ascii=False)										 
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ป้องกันยกเลิกเชิญบอทปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันยกเลิกเชิญบอทปิดใช้งาน"
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)                                                          

                        elif 'กันทั้งหมด ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('กันทั้งหมด ','')
                              if spl == 'เปิด':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "เปิดป้องกันทั้งหมดเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "เปิดป้องกันทั้งหมดเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันทั้งหมดเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    else:
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ปิดป้องกันทั้งหมดเรียบร้อย\nกลุ่ม : " +str(ginfo.name)
                                    aditmadzs.sendMessage(msg.to, "「TON BOT ILNE」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = aditmadzs.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           aditmadzs.updateGroup(G)
                                           invsend = 0
                                           Ticket = client.reissueGroupTicket(msg.to)
                                           g1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           g1.kickoutFromGroup(msg.to, [target])
                                           g1.leaveGroup(msg.to)
                                           X = aditmadzs.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           aditmadzs.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                        elif 'bye1' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        ki.kickoutFromGroup(msg.to,[target])
                                    except:
                                        ki.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")
                        elif 'bye2' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kk.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kk.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")   
                        elif 'bye3' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kc.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kc.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")
                        elif 'bye4' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        km.kickoutFromGroup(msg.to,[target])
                                    except:
                                        km.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")         
                        elif 'bye5' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kb.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kb.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")         
                        elif 'bye6' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kd.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kd.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")             
                        elif 'bye7' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        ke.kickoutFromGroup(msg.to,[target])
                                    except:
                                        ke.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")         
                        elif 'bye8' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kf.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kf.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")                                        
                        elif 'bye9' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kg.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kg.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ") 
                        elif 'bye0' in text.lower():
                            if msg._from in admin:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:                                      
                                        kh.kickoutFromGroup(msg.to,[target])
                                    except:
                                        kh.sendMessage(msg.to,"ใช้กือเตะทั้งวันจนกือพังหมดแล้วควยกือบัคแล้วยั้งจะให้เตะ")                                    

                        elif cmd == "refresh" or text.lower() == 'รีข้อมุล':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                aditmadzs.sendMessage(msg.to,"รีข้อมูลเรียบร้อย...")

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'เตะแทค เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดเตะคนแทคเรียบร้อย...")

                        elif cmd == "notag off" or text.lower() == 'เตะแทค ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดเตะคนแทคเรียบร้อย...")

                        elif cmd == "contact on" or text.lower() == 'อ่านตัส เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดอ่านตัสเรียบร้อย...")

                        elif cmd == "contact off" or text.lower() == 'อ่านตัส ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดอ่านตัสเรียบร้อย")

                        elif cmd == "respon on" or text.lower() == 'ตอบแทค เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดตอบแทคเวลาคนแทคเรียบร้อย...")

                        elif cmd == "respon off" or text.lower() == 'ตอบแทค ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"เปิดตอบแทคเวลาคนแทคเรียบร้อย...")
                                
                        elif cmd == "respongift on" or text.lower() == 'ส่งกิ๊ฟ เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดส่งติ๊กเวลาคนแทคเรียบร้อย...")

                        elif cmd == "respongift off" or text.lower() == 'ส่งกิ๊ฟ ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดส่งติ๊กเวลาคนแทคเรียบร้อย..")                                

                        elif cmd == "autojoin on" or text.lower() == 'เข้ากลุ่ม เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดเข้ากลุ่มออโต้เรียบร้อย...")

                        elif cmd == "autojoin off" or text.lower() == 'เข้ากลุ่ม ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดเข้ากลุ่มออโต้เรียบร้อย...")

                        elif cmd == "autoleave on" or text.lower() == 'ออกแชท เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดออกแชทรวมเรียบร้อย...")

                        elif cmd == "autoleave off" or text.lower() == 'ออกแชท ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดออกแชทรวมเรียบร้อย...")

                        elif cmd == "autoadd on" or text.lower() == 'บล็อค เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดออโต้บล็อคเรียบร้อย...")

                        elif cmd == "autoadd off" or text.lower() == 'บล็อค ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดออโต้บล็อคเรียบร้อย...")

                        elif cmd == "sticker on" or text.lower() == 'ลิ้งติ๊ก เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดลิ้งติ๊กเรียบร้อย...")

                        elif cmd == "sticker off" or text.lower() == 'ลิ้งติ๊ก ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"เปิดลิ้งติ๊กเรียบร้อย...")

                        elif cmd == "jointicket on" or text.lower() == 'มุดลิ้ง เปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"เปิดมุดลิ้งเรียบร้อย...")

                        elif cmd == "jointicket off" or text.lower() == 'มุดลิ้ง ปิด':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"ปิดมุดลิ้งเรียบร้อย...")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"แก้ขาวเรียบร้อย...")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"โปรดส่งคอลแทคคนทีจะลงดำลงมา...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"โปรดส่งคอลแทคคนทีจะแก้ดำลงมา...")

                        elif ("ดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"เพิ่มบัญชีดำเรียบร้อย...")
                                       except:
                                           pass

                        elif ("ขาว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"เพิ่มบัญชีขาวเรียบร้อย...")
                                       except:
                                           pass

                        elif cmd == "ดำ:เปิด" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"โปรดส่งคอลแทค...")

                        elif cmd == "ขาว:เปิด" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"โปรดส่งคอลแทค...")

                        elif cmd == "เชคดำ" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"รายชื่อผู้ติดดำทั้งหมด")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"⏩ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "คทดำ" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = aditmadzs.getContact(i)
                                        aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = aditmadzs.getContacts(wait["blacklist"])
                              mc = "「%i」ลบดำเรียบร้อย" % len(ragets)
                              aditmadzs.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              ki.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              kk.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              kc.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              km.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              kb.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc) 
                              kd.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              ke.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              kf.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              kg.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
                              kh.sendMessage(msg.to,"ล้างดำเรียบร้อย..." +mc)
#===========COMMAND SET============#
                        elif 'ตั้งตอบแอด: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งตอบแอด: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "ตั้งทักคนแอดมาเรียบร้อย...")
                              else:
                                  wait["message"] = spl
                                  aditmadzs.sendMessage(msg.to, "「ข้อคนแอดมาคือ」 :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งต้อนรับ: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งต้อนรับ: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "ตั้งต้อนรับเรียบร้อย..")
                              else:
                                  wait["welcome"] = spl
                                  aditmadzs.sendMessage(msg.to, "「ข้อต้อนรับคือ」 :\n\n「{}」".format(str(spl)))
                                  
                        elif 'ตั้งออก: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งออก: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "ตั้งออกเรียบร้อย...")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, "「ข้อความคนออกคือ」:\n\n「{}」".format(str(spl)))                                    

                        elif 'ตั้งแทค: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งแทค: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "ตั้งแทคเรียบร้อย...")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, "「ข้อความตอบคนแทคคืน」 :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ADITMADZSmessage1"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งทักคนยืน: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งทักคนยืน: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "ตั้งทักคนยืนเรียบร้อย...")
                              else:
                                  wait["mention"] = spl
                                  aditmadzs.sendMessage(msg.to, "「ข้อความทักคนยืนคืน」 :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Pesan Msg」\nPesan Message lu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "เชคเข้า":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「ข้อความคนเข้าคืน」「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "เชคออก":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「ข้อความคนออกคือ」「 " + str(wait["leave"]) + " 」")                                 

                        elif text.lower() == "เชคแทค":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「ข้อความตอบแทคคืน」「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「....」\n\n「 " + str(Setmain["ADITMADZSmessage1"]) + " 」")

                        elif text.lower() == "เชคยืน":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「ข้อความคนยืนคืน」:\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group1.id,ticket_id)                                     
                                     group1 = km.findGroupByTicket(ticket_id)
                                     km.acceptGroupInvitationByTicket(group1.id,ticket_id)                                     
                                     group1 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group1.id,ticket_id)                                     
                                     group1 = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group1.id,ticket_id)                                     
                                     group1 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group1.id,ticket_id)                                     
                                     group1 = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = kg.findGroupByTicket(ticket_id)
                                     kg.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group1 = kh.findGroupByTicket(ticket_id)
                                     kh.acceptGroupInvitationByTicket(group1.id,ticket_id)                                     
    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
