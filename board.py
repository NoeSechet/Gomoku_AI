#!/usr/bin/python3

import math
import random

import settings as set
from patterns import check_patterns

from dataclasses import dataclass

@dataclass
class Board:
    state: list
    size: int

    def __init__(self, size):
        self.size = size
        self.state = []
        for y in range (size):
            row = [set.PlaceStat(0, y) for i in range(size)]
            for x in range (size):
                row[x].x = x
            self.state.append(row)

    def print(self):
        for y in range (self.size):
            for x in range (self.size):
                print(self.state[y][x].val, end=' ')
            print('')

    def randomCoord(self):
        coord = set.Vec2(random.randint(0, self.size - 1), random.randint(0, self.size - 1))

        if self.state[coord.y][coord.x].val != '0':
            return self.randomCoord()

        return coord

    def randomFill(self, nbTurns):
        for x in range(nbTurns):
            coord = self.randomCoord()
            self.state[coord.y][coord.x].val = str(random.randint(1, 2))

    def dumbEvaluate(self):
        return 1

    def evaluate(self):

        score_res = 0

        for y in range (self.size):
            for x in range (self.size):
                if (self.state[y][x].val != '0'):
                    score = check_patterns(x, y)
                    score_res += score

        return score_res