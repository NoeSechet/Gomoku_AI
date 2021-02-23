#!/usr/bin/python3

import settings as s
from best_move import findBestMove

def display():
    s.board.print()


def start(arg):
    arg = arg.split(' ')[1]

    if int(arg) < 10:
        print('ERROR message - unsupported size or other error')
        return
    s.init(int(arg))
    print('OK')


def turn(arg):
    arg = arg.split(' ')
    position = arg[1].split(',')
    x = int(position[0])
    y = int(position[1])

    s.board.state[y][x].val = '2' # '2' represent opponent's stone
    AIMove = findBestMove()
    s.board.state[AIMove.y][AIMove.x].val = '1' # '1' represent own's stone
    print(str(AIMove.x) + ',' + str(AIMove.y))


def begin():
    AIMove = findBestMove()
    s.board.state[(AIMove.y)][(AIMove.x)].val = '1' # '1' represent own's stone
    print(str(AIMove.x) + ',' + str(AIMove.y))


def reconfigBoard():

    line = input().split(" ")

    while line[0] != "DONE":
        move = line[0].split(',')
        s.board.state[int(move[1])][int(move[0])].val = move[2]
        line = input().split(" ")

    begin()


def quit():
    exit(0)

def about():
    print("name=\"LazyStudents\", version=\"1.0\", author=\"ArnaudNoé\", country=\"FR\"")