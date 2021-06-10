import glob
import time
from functools import reduce
import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Удачной работы, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)


############## СКРИПТ ОБРАБОТЧИК ##################
test_text = input ("Нажми кнопку получить")

if test_text == 'new':
    f = open("New.txt","r+")
    s = (f.read())
    s = s.split(sep='\n')
    a = str.split(s[0], sep=':')
    print(a[0])
    time.sleep(1)
    print(a[1])
else:
    print('Нажми на кнопку!')

Done = input('Успешно вошел в аккаунт?')

if Done == "Yes":
    file = open("Использован.txt", "a+")
    file.write('\n'+str(a[0])+":"+str(a[1]))
    file.close()
elif Done == "Nope":
    file = open("Ошибка.txt", "a+")
    file.write('\n'+str(a[0])+":"+str(a[1]))
    file.close()
else:
    print('Ответь на вопрос, пожалуйста')

with open("New.txt", "r") as file:
    lines = file.readlines()
del lines[0]
with open("New.txt", "w") as file:
    file.writelines(lines)

f.close()



PlusTik = input('Скидывай акки')
T = PlusTik
file = open("New.txt", "a+")
file.write(T+'\n')
file.close()





