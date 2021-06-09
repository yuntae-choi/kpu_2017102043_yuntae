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


import notic




def replyAptData(dastr, user, Input_Entry):
    print(user, dastr, Input_Entry)
    today = date.today()
    todaystr = today.strftime('%Y%m%d')
    print(dastr,todaystr, Input_Entry)
    res_list = notic.getData(dastr,todaystr)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>notic.MAX_MSG_LENGTH:
            notic.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        notic.sendMessage( user, msg )
    else:
        notic.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%date_param )

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        notic.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        notic.sendMessage( user, '저장되었습니다.' )
        conn.commit()

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        notic.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        notic.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('물품') and len(args) > 1:
        print('try to 물품', args[1])
        replyAptData(args[1], chat_id, args[2] )
    elif text.startswith('저장') and len(args) > 1:
        print('try to 저장', args[1])
        save(chat_id, args[1])
    elif text.startswith('확인'):
        print('try to 확인')
        check(chat_id)
    else:
        notic.sendMessage(chat_id, """모르는 명령어입니다. 물품 물품명 찾을 날짜를 입력해주세요 \n 물품 지갑 20210605 """)

today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', notic.TOKEN )

bot = telepot.Bot(notic.TOKEN)
print( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)