# -*- coding: utf-8 -*-
import Helper
import telebot
from telebot import apihelper
from telebot import types
import sqlite3
import sql
import random
#from pip.commands import commands
import time
import Names


bot = telebot.TeleBot("1082552377:AAGGwJKQ9llMm7x4kmCLxaIVw0TnAyJ13eM")
@bot.message_handler(commands=['start'])
def start(message):
    sql1 = sql.sql()
    if(sql1.select(message.chat.id)):
        bot.send_message(message.chat.id,
                         "Добро пожаловать",
                         parse_mode="Markdown", reply_markup=Menu())
    else:
        sql1.regisrt(message.chat.id)
        print("Зарегестрировали "+str(message.chat.id))
        bot.send_message(message.chat.id,
                         "Введите город",
                         parse_mode="Markdown")
        
@bot.message_handler(commands=['admin'])
def adm(message):
    if(str(message.chat.id) == "296823509" ):
        bot.send_message(message.chat.id, "Добро пожаловать, лохебаный",parse_mode="Markdown",reply_markup=Adminmenu())
    

    sqool = sql.sql()
    hlp = Helper.Helper()
    do25 = hlp.filesdo25()
    posle25 = hlp.filesposle25()
    im = Names
    while(True):
        randdo25 = random.randint(0,len(do25))-1
        randposle25 = random.randint(0,len(posle25))-1
        if(randdo25 == -1 or randposle25 == -1):
            continue
        break
    while(True):
        if(sqool.cityregret(message.chat.id) == 0):
            sqool.addcity(message.chat.id, message.text)
            sqool.zerotoone(message.chat.id)
            bot.send_message(message.chat.id,"Выберите возраст",parse_mode="Markdown",reply_markup=Menu())
            print("1")
            break
        else:
            if(message.text == "Познакомиться после 25"):
                photo = open(posle25[randposle25], 'rb')
                try:
                    bot.send_photo(message.chat.id, photo,randomname(),reply_markup=inlkeyboardposle25())
                    break
                except:
                    print("Ошибка #1")
                    continue
            elif(message.text == "Познакомиться до 25"):
                photo = open(do25[randdo25], 'rb')
                try:
                    bot.send_photo(message.chat.id, photo,randomname(),reply_markup=inlkeyboarddo25())
                    break
                except:
                    print("Ошибка #2")
                    continue
            elif(str(message.chat.id) == "296823509" and message.text == "Статистика"):
                try:
                    bot.send_message(message.chat.id,sqool.statistika())
                    break
                except:
                    print("Ошибка #3")
                    continue

def inlkeyboarddo25():
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text=randominst(),url="http://ykako.milfalone.com/c/da57dc555e50572d?s1=4568&s2=16070&s3=1&click_id=123")
    url_button2 = types.InlineKeyboardButton(text="Познакомиться", url="https://hookups11.com/?u=pf1k605&o=3bnp2b8")
    keyboard.add(url_button1)
    keyboard.add(url_button2)
    return keyboard
def inlkeyboardposle25():
    keyboard = types.InlineKeyboardMarkup()
    url_button1 = types.InlineKeyboardButton(text=randominst(),url="http://ykako.milfalone.com/c/da57dc555e50572d?s1=4568&s2=16070&s3=1&click_id=123")
    url_button2 = types.InlineKeyboardButton(text="Познакомиться", url="https://hookups11.com/?u=pf1k605&o=3bnp2b8")
    keyboard.add(url_button1)
    keyboard.add(url_button2)
    return keyboard
def randomname():
    im = Names
    x = random.randint(0,len(im.Imya))
    return Names.Imya[x]
def randominst():
    ins = Names
    x = random.randint(0,len(ins.Insta))
    return Names.Insta[x]
def Main():
    helper = Helper.Helper()
    helper.log("бот запущен")
    botpolling()
    
def botpolling():
    PROXY = '8XLgrh:a4szaK@213.166.74.250:9788' #(Логин и пароль от купленного прокси)
    apihelper.proxy = {'https':'https://' + PROXY}  
    while(True):
        try:
            bot.polling(none_stop = True,timeout=300)
        except:
            print("Ошибка #Main")
            time.sleep(300)
            continue   
       
def Adminmenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    item1 = types.KeyboardButton("Статистика")
    markup.add(item1)
    return markup

def Menu():

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    item1 = types.KeyboardButton("Познакомиться до 25")
    item2 = types.KeyboardButton("Познакомиться после 25")
    markup.add(item1, item2)
    return markup

if __name__ == "__main__":
    Main();


    























