import sqlite3
import InputDB
import Output
import telebot


bot = telebot.TeleBot('1122158709:AAGrNF_UmJD0dt6Tr5Pq6ynYHvs10UkdoLg')

def Pog(message):
    a  = message.text.split(" ")
    InputDB.InputDB(a[0], a[1], a[2])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}. Напишите, что вы хотите сделать:\n Записать в таблицу \n Показать данные из таблицы')

@bot.message_handler(commands=['inp'])
def get_input_db(message):
    a = bot.send_message(message.from_user.id, "Введите далее Страну, тип транспорта и цену поездки для заполнения базы данных.")
    #Следующая команда ждет ответа от пользователя и отсылает этот ответ в функцию Pog(), бот будет ждать жо последнего дня
    bot.register_next_step_handler(a,Pog)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global i
    if message.text == "Записать в таблицу":
        bot.send_message(message.from_user.id,"Введите название страны, средство передвижение и стоимость проезда, для заполнения базы данных с использование /inp")
    if message.text == "Показать данные из таблицы":
        i = ""
        b = Output.OutputDB()
        #Великое чудо Расима, считаю этот код божественным, но сам создатель в ужасе от созданного
        for d in range(len(b)):
            i = i + str(d + 1) + " "
            for f in b[d]:
                i = i + f + " "
                if f == b[d][-1]:
                    i += "\n"
        bot.send_message(message.from_user.id, text=i)


bot.polling()
