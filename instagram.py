
import telebot
# import api
import os
import instaloader
from PIL import Image

test = instaloader.Instaloader()
API_KEY = "1872907930:AAEKeNOVM770jwCPp8L0o5REWCr-Xo7RVFQ"
bot = telebot.TeleBot(API_KEY, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "welcome to the bot🖐️🖐️\n send me anyone instagram username to get their DP\n ex: virat.kohli, thenameisyash etc ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    acc = message.text
    p = test.download_profile(acc, profile_pic_only=True)
    path = (os.path.join(os.getcwd(), acc))
    for i in os.listdir(path):
        if "jpg" in i or "jpeg" in i:
            path = os.path.join(path, i)
            break
    im = Image.open(path)
    # print(type(p))
    bot.send_photo(message.chat.id, im, "Profile picture")


bot.polling()
