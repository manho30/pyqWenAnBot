import telebot
import requests

bot = 'UR_TOKEN', parse_mode=None)

@bot.message_handler(content_types=['text'])
def handleMessage(m):
    return bot.reply_to(m, requests.get('https://api.shadiao.app/pyq').json().get('data').get('text'))
