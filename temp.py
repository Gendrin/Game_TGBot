
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#
#
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
#
#
# app = ApplicationBuilder().token("YOUR TOKEN HERE").build()
#
# app.add_handler(CommandHandler("hello", hello))
#
# app.run_polling()


# import emoji
# from isOdd import isOdd
# from progress.bar import Bar
# import time
# print(isOdd(0))
# print(isOdd(4))
# print(emoji.emojize('Python is :thumbs_up:'))
# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5664442295:AAGp5Zv0mdVbKJCwRqd9Fc3qdI3zUobl-UM").build()

app.add_handler(CommandHandler("hello", hello))

print('Server start')

app.run_polling()


#
#
# print(isOdd(1))
# #print(isOdd('5'))
#
# print(isOdd(0))
# print(isOdd(4))