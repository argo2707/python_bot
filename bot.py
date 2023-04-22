import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException
import time
bot = telebot.TeleBot('5869861728:AAHGnHorclpApCWhICqNpkrymOK2AdD3JnQ')

def is_subscribed(chat_id,user_id):
    chat_member =  bot.get_chat_member(chat_id=chat_id,user_id=user_id)
    print(chat_member.status)
    if  chat_member.status!='left':
        return  True
    else:
        return  False

@bot.message_handler(commands=["start"])
def start(message:types.Message, res=False):
    time.sleep(1)
    try:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        item1=types.KeyboardButton("Да"+ u'😍')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Привет!\nТы за бесплатной методичкой?',reply_markup=markup)
    except ApiTelegramException as e:
           if e.description == "Forbidden: bot was blocked by the user":
                   print("Attention please! The user {} has blocked the bot.".format(message.chat.id))
                   #bot.stop_polling()
                   #bot.polling(none_stop=True, interval=0)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def text(message):
        time.sleep(1)
        try:
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
            item1=types.KeyboardButton("Подписку оформил"+ u'😉')
            if is_subscribed(chat_id='@nftparty',user_id=message.from_user.id):
                doc = open('metodicka-2022.pdf', 'rb')
                bot.send_document(message.chat.id,doc)
                doc.close()
            else:
                markup.add(item1)
                bot.send_message(message.chat.id, "Подпишись на канал, друг!\nИ бесплатная методичка твоя!\n\nNFT БРИХАСПАТИ"+ u'👉'+"https://t.me/+X6Qj-bN8UY03NjZi",reply_markup=markup)
        except ApiTelegramException as e:
           if e.description == "Forbidden: bot was blocked by the user":
                   print("Attention please! The user {} has blocked the bot. I can't send anything to them".format(message.chat.id))
                   #bot.stop_polling()
                   #bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            time.sleep(3)
            print(e)