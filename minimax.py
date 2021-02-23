#!/usr/bin/python3

import math

import settings as s

def minimax(depth, alpha, beta, maximizing):
    gameOver = False
    if (depth == 0 or gameOver):
        return s.board.evaluate()

    if maximizing:
        maxEval = -math.inf
        for x in range(s.board.size):
            for y in range(s.board.size):
                if (s.board.state[y][x].val == '0'):
                    s.board.state[y][x].val = '1'
                    evalVal = minimax(depth - 1, alpha, beta, False)
                    s.board.state[y][x].val = '0'
                    maxEval = max(maxEval, evalVal)
                    # alpha = max(alpha, evalVal)
                    # if (beta <= alpha):
                    #     return maxEval
        return maxEval
    else:
        minEval = math.inf
        for x in range(s.board.size):
            for y in range(s.board.size):
                if (s.board.state[y][x].val == '0'):
                    s.board.state[y][x].val = '2'
                    evalVal = minimax(depth - 1, alpha, beta, True)
                    s.board.state[y][x].val = '0'
                    minEval = min(minEval, evalVal)
                    # beta = min(beta, evalVal)
                    # if (beta <= alpha):
                    #     return minEval
        return minEval