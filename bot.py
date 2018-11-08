import socket
import telebot
from telebot import apihelper

import config


apihelper.proxy = config.PROXY
BOT = telebot.TeleBot(config.TOKEN)


@BOT.message_handler(commands=['start'])
def send_start(message):
    BOT.reply_to(message, "Wop. Type \"notify\" to recieve notifications about tasks")


@BOT.message_handler(commands=['notify'])
def send_notification(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((config.HOST, config.PORT))
        
        while True:
            s.listen()
            connect, addr = s.accept()

            with connect:
                while True:
                    data = connect.recv(4096)
                    if not data:
                        break
                    
                    BOT.reply_to(message, data)


BOT.polling(none_stop=True, timeout=60)
