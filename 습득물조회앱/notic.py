#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import requests, xmltodict
TOKEN = '1733610303:AAFwnfK6-QltiaTNUw9QdNj1oV_or7Ofhng'
MAX_MSG_LENGTH = 100
key = "A762Mvt41oxxLGNbDOqSVdZ0o70TqIdu%2BasUtVXihiiC7Een2bHDYGp1CKesvBHiEda3tQ%2B5FFhfQoOY%2B0Vnfg%3D%3D"
baseurl = "http://apis.data.go.kr/1320000/LosfundInfoInqireService"

bot = telepot.Bot(TOKEN)


def getData(da_str,todaystr):
    res_list = []
    url = baseurl+"/getLosfundInfoAccToClAreaPd?"+"&serviceKey="+key+'&START_YMD='+da_str+'&END_YMD='+todaystr+"&N_FD_LCT_CD=LCA000"+'&pageNo=1'+'&numOfRows=10'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'xml')
    names = soup.find_all('item')
    for n in names:
        str = n.find('fdYmd').get_text()+"/"+n.find('depPlace').get_text()+"\n"+n.find('fdSbjt').get_text()
        res_list.append(str)
    return res_list


def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(todaystr, dastr= "20210605",Input_Entry="지갑"):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]

        res_list = getData(dastr,todaystr , Input_Entry)
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( str(datetime.now()).split('.')[0], r )
                if len(r+msg)+1>MAX_MSG_LENGTH:
                    sendMessage( user, msg )
                    msg = r+'\n'
                else:
                    msg += r+'\n'
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current = today.strftime('%Y%m%d')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current)
