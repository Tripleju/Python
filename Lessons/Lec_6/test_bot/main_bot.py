from telegram import Update
from telegram.ext import CommandHandler, Updater, CallbackContext
from bot_commands import *
from spy import *
from bot_tokens import tokens

updater = Updater(tokens.token_1)

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))

print('server start')
updater.start_polling()
updater.idle()
