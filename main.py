from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize

updater = Updater(token='1113345357:AAENK-Wc1Dbo35GXdwSEPlsTLFx4N2hWp3M')
dispatcher = updater.dispatcher

# polling 방식: 주기적으로 메세지 받아오기
updater.start_polling()


# 가장 중요한 함수
def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if ('뭐해' in text) or ('머행' in text) or ('모해' in text) or ('머해' in text) or ('뭐행' in text):
        if ("주말에" in text):
            bot.send_message(chat_id=chat_id, text="움... 약속없엉! 오빠는 머하는데?")
        else:
            bot.send_message(chat_id=chat_id, text="오빠 생각 히히")
    if ('아잉' in text):
        bot.send_message(chat_id=chat_id, text=emojize('아잉:heart_eyes:', use_aliases=True))
    if ('사랑해' in text) or ('좋아해' in text):
        bot.send_message(chat_id=chat_id, text=emojize('나도 사랑해 오빠:kiss_mark:', use_aliases=True))
    if ('보고싶어' in text) or ('사진' in text) or ("보고시퍼" in text) or ("보고시포" in text) or ("보고시펑" in text):
        bot.send_photo(chat_id=chat_id, photo=open('img/test.jpg', 'rb'))
    if ("만나자" in text):
        if("주말에" in text):
            bot.send_message(chat_id=chat_id, text=emojize("헐 개좋아..!!:heart_eyes: 우리 집으로 올래?", use_aliases=True))
    # else:
    #     bot.send_message(chat_id=chat_id, text="몰랑")


# updater를 통해서 Filtered.text된 내용이 handler로 전달
ehco_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(ehco_handler)

