import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from bot_tokens import tokens

logging.basicConfig(
level=logging.DEBUG,
filename="mybot_XO_log.log",
format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
datefmt='%d-%m-%Y %H:%M:%S',
)

# Включим ведение журнала
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
INPUTS=0

board = list(range(1,10))
counter = 0
win = False
X=chr(10060)
O=chr(11093)
valid = False
player_token=X

# Функция для отрисовки поля
def draw_board(board):
    txt = ''
    for i in range(len(board)):
        if not i % 3:
            txt += f'\n{"-" * 25}\n'
        txt += f'{board[i]:^8}'
    txt += f"\n{'-' * 25}"
    return txt

# функция обратного вызова точки входа в разговор
def start(update,_):
    global counter, win, X, O
    update.message.reply_text("Привет! давай поиграем в крестики-нолики!\n Команда /cancel, если захочешь выйти из игры.")
    update.message.reply_text(draw_board(board))
    update.message.reply_text("Куда поставим " + X+"? ")
    return INPUTS

def main(update, _):
    global win, counter, player_token, valid
   
    player_answer = update.message.text
    try:
        player_answer=int(player_answer)
        if str(board[player_answer-1]).isdigit()==False:
            update.message.reply_text(f"{chr(10071)} Эта клеточка уже занята")
        else:
            if player_answer not in board:
                update.message.reply_text(f"{chr(9940)} Некорректный ввод. Введите число от 1 до 9.")
            else:
                board[player_answer-1]=player_token
                update.message.reply_text(draw_board(board))
                if counter > 3:
                    tmp = check_win(board)
                    if tmp:
                        update.message.reply_text(f'{tmp} выиграл! {chr(129395)}')
                              
                        return ConversationHandler.END
                if counter % 2 == 0:
                    player_token=O
                else:
                    player_token=X    
                counter += 1
                
        
        if counter < 9:
            update.message.reply_text("Куда поставим " + player_token+"? ")
        elif counter == 9:
            update.message.reply_text(f"{chr(129309)} Ничья!")
            return ConversationHandler.END

    except:
        if player_answer=='/cancel':
            cancel(update, _)
            return ConversationHandler.END
        else:
            update.message.reply_text(f"{chr(9940)} Некорректный ввод. Вы уверены, что ввели число?")



def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False   


def cancel(update, _):
    update.message.reply_text('До связи!', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(tokens.token_2)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            INPUTS: [MessageHandler(Filters.text, main),CommandHandler('cancel', cancel)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`

    dispatcher.add_handler(conv_handler)

    # Запуск бота
    print('server start')
    updater.start_polling()
    updater.idle()