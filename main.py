from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types


token = "6122808705:AAESj1Xr7rqewcxKALtL3_JwlODNE9Q1rAA"
bot = telebot.TeleBot(token)

url = requests.get("https://www.basketball-reference.com/leagues/NBA_2023.html")
soup = BeautifulSoup(url.text, "html.parser")


@bot.message_handler(commands=["start"])
def start_message(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Hi, show me what you can do")
    markup1.add(but1)
    bot.send_message(message.chat.id, "Hello!", reply_markup=markup1)


@bot.message_handler(content_types=["text"])
def button_message(message):
    global markup2
    fil_division = []
    division = list(soup.findAll(class_="thead"))

    for data in division:
        if data.find("Division") != 0:
            fil_division.append(data.text)

    if message.text == "Hi, show me what you can do":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in fil_division:
            markup2.add(types.KeyboardButton(i))
        bot.send_message(message.chat.id, "Choose division", reply_markup=markup2)

    back_to_div = types.KeyboardButton("Back to divisions")

    if message.text == "Back to divisions":
        bot.send_message(message.chat.id, "Choose division", reply_markup=markup2)

    if message.text == "Atlantic Division":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bos = types.KeyboardButton("Boston Celtics")
        phi = types.KeyboardButton("Philadelphia 76ers")
        nyk = types.KeyboardButton("New York Knicks")
        bkn = types.KeyboardButton("Brooklyn Nets")
        tor = types.KeyboardButton("Toronto Raptors")
        markup3.add(bos, phi, nyk, bkn, tor, back_to_div)
        bot.send_message(message.chat.id, "Choose team", reply_markup=markup3)

    elif message.text == "Central Division":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mil = types.KeyboardButton("Milwaukee Bucks")
        cle = types.KeyboardButton("Cleveland Cavaliers")
        chi = types.KeyboardButton("Chicago Bulls")
        pac = types.KeyboardButton("Indiana Pacers")
        det = types.KeyboardButton("Detroit Pistons")
        markup3.add(mil, cle, chi, pac, det, back_to_div)
        bot.send_message(message.chat.id, "Choose team", reply_markup=markup3)

    elif message.text == "Southeast Division":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mia = types.KeyboardButton("Miami Heat")
        atl = types.KeyboardButton("Atlanta Hawks")
        was = types.KeyboardButton("Washington Wizards")
        mag = types.KeyboardButton("Orlando Magic")
        cho = types.KeyboardButton("Charlotte Hornets")
        markup3.add(mia, atl, was, mag, cho, back_to_div)
        bot.send_message(message.chat.id, "Choose team", reply_markup=markup3)

    elif message.text == "Northwest Division":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        den = types.KeyboardButton("Denver Nuggets")
        tim = types.KeyboardButton("Minnesota Timberwolves")
        okc = types.KeyboardButton("Oklahoma City Thunder")
        uth = types.KeyboardButton("Utah Jazz")
        por = types.KeyboardButton("Portland Trail Blazers")
        markup3.add(den, tim, okc, uth, por, back_to_div)
        bot.send_message(message.chat.id, "Choose team", reply_markup=markup3)

    elif message.text == "Pacific Division":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sac = types.KeyboardButton("Sacramento Kings")
        pho = types.KeyboardButton("Phoenix Suns")
        lac = types.KeyboardButton("Los Angeles Clippers")
        gsw = types.KeyboardButton("Golden State Warriors")
        lal = types.KeyboardButton("Los Angeles Lakers")
        markup3.add(sac, pho, lac, gsw, lal, back_to_div)
        bot.send_message(message.chat.id, "Choose team", reply_markup=markup3)

    elif message.text == "Southwest Division":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mem = types.KeyboardButton("Memphis Grizzlies")
        nop = types.KeyboardButton("New Orleans Pelicans")
        dal = types.KeyboardButton("Dallas Mavericks")
        hou = types.KeyboardButton("Houston Rockets")
        sas = types.KeyboardButton("San Antonio Spurs")
        markup3.add(mem, nop, dal, hou, sas, back_to_div)
        bot.send_message(message.chat.id, "Choose team", reply_markup=markup3)
    
    
bot.polling(none_stop=True)
