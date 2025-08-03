import telebot
import random
from confid import token
import os
print(os.listdir('images'))
token="8152462480:AAH600JnTOrH6w_jac-LX2LkU0mi03yvaXk"


# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот для Защиты окружающей среды чем могу помочь?Команды:/glass,/plastic,/paper,/aluminum,/iron,/wet_wipes")

@bot.message_handler(commands=["glass"])
def send_glass(message):
    bot.reply_to(message, "По оценкам некоторых исследований, для разрушения стекла требуется около миллиона лет. Однако есть и другие мнения: некоторые учёные считают, что стекло не разлагается, а просто разрушается.")

@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    bot.reply_to(message, "Разложение пластика может занимать от десятков до сотен лет. Точный срок зависит от вида материала и условий, в которых он находится.")

@bot.message_handler(commands=["paper"])
def send_paper(message):
    bot.reply_to(message, "Время разложения бумаги зависит от типа материала и условий окружающей среды. В естественной среде (в почве или компостной куче) обычная бумага разлагается за 2–6 недель. Гофрированный картон — 3 месяца — 1 год.")

@bot.message_handler(commands=["aluminum"])
def send_uminalum(message):
    bot.reply_to(message, "Период полного разложения алюминия — один из самых длительных среди современных материалов. Это связано с тем, что алюминий устойчив к коррозии и может сохранять свои свойства в течение длительного времени.")

@bot.message_handler(commands=["iron"])
def send_iron(message):
    bot.reply_to(message, "Металлолом из железа разлагается под действием кислорода, в конечном итоге образуя оксид железа. Скорость разложения металлических изделий: за 10–20 лет на один миллиметр в глубину (в пресной воде — за 3–5 лет, в солёной — за год-два")

@bot.message_handler(commands=["wet_wipes"])
def send_wet_wipes(message):
    bot.reply_to(message, "Срок разложения влажных салфеток зависит от их состава и может быть от 50 до 500 лет. На скорость разложения влияют такие факторы, как температура воздуха, вода и кислород.")

@bot.message_handler(commands=['mem1'])
def send_mem(message):
    with open('images/mem1.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem2'])
def send_mem(message):
    with open('images/mem2.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem4'])
def send_mem(message):
    with open('images/mem4.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem5'])
def send_mem(message):
    with open('images/mem5.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem6'])
def send_mem(message):
    with open('images/mem6.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()
