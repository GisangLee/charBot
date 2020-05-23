import telegram
api_key = 'key'
bot = telegram.Bot(token=api_key)


# chat_id = bot.get_updates()[-1].message.chat_id
# 위 코드는 chat_id를 찾는 방법
chat_id = 1000539293

bot.sendMessage(chat_id=chat_id, text="기상아 안녕?")


# for i in bot.getUpdates():
#     print(i)
#     print()





