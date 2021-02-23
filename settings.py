#!/usr/bin/python3

import board as b

from dataclasses import dataclass

@dataclass
class Vec2:
    x: int
    y: int

@dataclass
class PlaceStat:
    x: int
    y: int
    val: bytes
    row_chk: bool
    col_chk: bool
    diag_d_chk: bool
    diag_u_chk: bool

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = '0'
        self.row_chk = False
        self.col_chk = False
        self.diag_d_chk = False
        self.diag_u_chk = False

def init(size):
    global board
    global found_pattern

    board = b.Board(size)
    found_pattern = False