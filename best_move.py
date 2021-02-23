#!/usr/bin/python3

import math

import settings as s
from minimax import minimax

def findBestMove():
    s.found_pattern = False
    bestScore = -math.inf
    bestMove = s.Vec2(0, 0)

    for y in range(s.board.size):
        for x in range(s.board.size):
            if (s.board.state[y][x].val == '0'):
                s.board.state[y][x].val = '1'
                score = minimax(0, -math.inf, math.inf, False)
                s.board.state[y][x].val = '0'
                # if (x == 9 and y == 5):
                #     print("score when 9,5: ", score)
                # print("best =", bestScore)

                if (score > bestScore):
                    # print("new score:", score)
                    # print("x = " + str(x) + ", y = " + str(y))
                    bestScore = score
                    bestMove.x = x
                    bestMove.y = y
    if (bestScore == 0 and s.found_pattern == False):
        bestMove = s.board.randomCoord()
        # print('random')
    return bestMove