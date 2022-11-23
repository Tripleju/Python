#3.* Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи
# https://unicode-table.com/ru/emoji/

# подумаю об этом завтра. сегодня уже не могу.

	
# -*- coding: utf-8 -*-

# board = range(1,10)

# def draw_board(board):
#     print ''
#     for i in range(3):
#         print "|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|"
#         print ''

# draw_board(board)

# print(1)

# Инициализация карты
maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Вывод карты на экран
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    