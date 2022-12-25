import requests
from bs4 import BeautifulSoup as b
from telebot import TeleBot
bot = TeleBot('5840368956:AAG9AdmUBT3R_tkZ0hbtp25uQkutCRKzzEg')


@bot.message_handler(commands=['start'])
def start(message):
    string = "Привет! я УМЕЮ показывать курс валюты (доллары, евро и юани)"
    bot.send_message(message.chat.id, string, parse_mode='html')


@bot.message_handler(commands=['dollar'])
def dollar(message):
    url = 'https://cbr.ru/key-indicators/'
    r = requests.get(url)
    soup = b(r.text, 'lxml')
    string = soup.find("td", class_="value td-w-4 _bold _end mono-num")
    string = string.text
    bot.send_message(message.chat.id, string)


@bot.message_handler(commands=['euro'])
def dollar(message):
    url = 'https://cbr.ru/key-indicators/'
    r = requests.get(url)
    soup = b(r.text, 'lxml')
    string = soup.find_all("td", class_="value td-w-4 _bold _end mono-num")[1]
    string = string.text
    bot.send_message(message.chat.id, string)


@bot.message_handler(commands=['yuan'])
def dollar(message):
    url = 'https://cbr.ru/key-indicators/'
    r = requests.get(url)
    soup = b(r.text, 'lxml')
    string = soup.find_all("td", class_="value td-w-4 _bold _end mono-num")[2]
    string = string.text
    bot.send_message(message.chat.id, string)


bot.polling(none_stop=True)

