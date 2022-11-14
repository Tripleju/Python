from telegram import Update
from telegram.ext import CommandHandler, Updater, CallbackContext
from bot_commands import *
from spy import *


updater = Updater("5798233180:AAE1QkxOkra9SaNSjleonf6OtUQvRWWWlGo")

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))

print('server start')
updater.start_polling()
updater.idle()
