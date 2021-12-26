import sqlite3
import InputDB
import Output
import telebot


bot = telebot.TeleBot('')

def Pog(message):
    try:
        a  = message.text.split(" ")
        InputDB.InputDB(a[0], a[1], a[2])
        bot.reply_to(message, 'Данные были введены')
    except (IndexError, TypeError, AttributeError):
        bot.reply_to(message, 'Вы ввели данные не по образцу')
        get_input_db(message)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}. Напишите, что вы хотите сделать:\n Записать в таблицу \n Показать данные из таблицы')

@bot.message_handler(commands=['inp'])
def get_input_db(message):
    a = bot.reply_to(message, "Введите далее Страну, тип транспорта и цену поездки для заполнения базы данных.")
    #Следующая команда ждет ответа от пользователя и отсылает этот ответ в функцию Pog(), бот будет ждать жо последнего дня
    bot.register_next_step_handler(a,Pog)
@bot.message_handler(commands=['db'])
def give_output_db(message):
        i = ""
        b = Output.OutputDB()
        #Великое чудо Расима, считаю этот код божественным, но сам создатель в ужасе от созданного
        for d in range(len(b)):
            i = i + str(d+1) + " "
            for f in b[d]:
                i = i + f + " "
                if f == b[d][-1]:
                    i += "\n"
        if len(i) > 4096:
            a = len(i)
            n = 0
            b = 0
            while a > 4096:
                b += 4096
                bot.reply_to(message, text = i[n:b])
                n+=4096
                a -= 4096
            if a > 0:
                bot.reply_to(message, text = i[n:n+a])
        else:
            bot.reply_to(message, text=i)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global i
    if message.text == "Записать в таблицу":
        bot.reply_to(message,"Введите название страны, средство передвижение и стоимость проезда, для заполнения базы данных с использование /inp")


bot.polling()
