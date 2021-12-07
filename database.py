import sqlite3
import InputDB
import Output
import telebot


bot = telebot.TeleBot('1122158709:AAGrNF_UmJD0dt6Tr5Pq6ynYHvs10UkdoLg')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}. Напишите, что вы хотите сделать:\n Записать в таблицу \n Показать данные из таблицы')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global i
    if message.text == "Записать в таблицу":
        #Необходимо будет вынести это в цикл для более удобного использования, без обязательного ввода данных при каждом запуске
        bot.send_message(message.from_user.id,"Введите название страны, средство передвижение и стоимость проезда, для заполнения базы данных с использование /db")
    if message.text == "Показать данные из таблицы":
        i = ""
        b = Output.OutputDB()
        for d in range(len(b)):
            for f in b[d]:
                i = i + f + " "
                if f == b[d][-1]:
                    i += "\n"
        bot.send_message(message.from_user.id, text=i)
        #Каким-то чудом переделывает массив b в нумерованную строку с помощью enumerate
            #Как это сделать, чтобы отправлялся текст, ну или таблица с данными, я честно хз, пытаюсь понять но не могу, расим помоги
    if message.text.startswith("/db"):
        a = message.text[3:].split(" ")
        InputDB.InputDB(a[0],a[1],a[2])
bot.polling()
