#3.* Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи
# https://unicode-table.com/ru/emoji/

	
# -*- coding: utf-8 -*-

board = list(range(1,10))

def draw_board(board):
    print('-------------')
    for i in range(3):
        print("|", board[0+i*3],"|", board[1+i*3],"|",  board[2+i*3],"|")
        print('-------------')

draw_board(board)

def step_maps(step,symbol):
    ind = board.index(step)
    board[ind] = symbol

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print(f"{chr(9940)} Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[player_answer-1]).isdigit():
                board[player_answer-1]=player_token
                valid = True
            else:
                print(f"{chr(10071)} Эта клеточка уже занята")
        else:
            print(f"{chr(9940)} Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False   

def main(board):
    counter = 0
    win = False
    X=chr(10060)
    O=chr(11093)
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(X)
        else:
            take_input(O)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(f'{tmp} выиграл! {chr(129395)}')
                win = True
                break
        if counter == 9:
            print(f"{chr(129309)} Ничья!")
            break
    draw_board(board)

main(board)