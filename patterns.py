#!/usr/bin/python3

import settings as s

patterns = {
    '111110': 1000000000000000,
    '222220': -9999999999,
    '011111': 1000000000000000,
    '022222': -9999999999,

    '011110': 100000000,
    '022220': -99999999,

    '211110': 10000000,
    '122220': -9999999,
    '011112': 10000000,
    '022221': -9999999,

    '111010': 10000000,
    '111012': 10000000,
    '210111': 10000000,
    '010111': 10000000,
    '211011': 10000000,
    '011011': 10000000,
    '110112': 10000000,
    '110110': 10000000,
    '222020': -9999999,
    '222021': -9999999,
    '120222': -9999999,
    '020222': -9999999,
    '122022': -9999999,
    '022022': -9999999,
    '220221': -9999999,
    '220220': -9999999,

    '011100': 1000,
    '011102': 1000,
    '001110': 1000,
    '201110': 1000,
    '022200': -999,
    '022201': -999,
    '002220': -999,
    '102220': -999,

    '111000': 50,
    '111002': 50,
    '000111': 50,
    '200111': 50,

    '211100': 50,
    '122200': -49,

    '222000': -49,
    '222001': -49,
    '000222': -49,
    '100222': -49,

}


def get_horizontals(x, y):

    hori_str = ""

    for i in range(x - 3, x + 3):
        if i >= s.board.size or i < 0:
            hori_str = ""
            break
        hori_str += s.board.state[y][i].val

    return hori_str


def get_verticals(x, y):

    vert_str = ""

    for i in range(y - 3, y + 3):
        if i >= s.board.size or i < 0:
            vert_str = ""
            break
        vert_str += s.board.state[i][x].val

    return vert_str


def get_right_down_diagos(x, y):

    r_d_diag_str = ""

    k = y - 3
    for i in range(x - 3, x + 3):
        if i >= s.board.size or i < 0 or k >= s.board.size or k < 0:
            r_d_diag_str = ""
            break
        r_d_diag_str += s.board.state[k][i].val
        k += 1

    return r_d_diag_str


def get_right_up_diagos(x, y):

    r_u_diag_str = ""

    k = y + 3
    for i in range(x - 3, x + 3):
        if i >= s.board.size or i < 0 or k >= s.board.size or k < 0:
            r_u_diag_str = ""
            break
        r_u_diag_str += s.board.state[k][i].val
        k -= 1

    return r_u_diag_str


def get_string_score(my_str):
    try:
        score = patterns[my_str]
        # print("checked str =", my_str)
        # print("checked score =", score)
        return score
    except:
        return 0


def check_patterns(x, y):

    score = 0

    potential_key_list = []

    potential_key_list.append(get_horizontals(x, y))
    potential_key_list.append(get_verticals(x, y))
    potential_key_list.append(get_right_down_diagos(x, y))
    potential_key_list.append(get_right_up_diagos(x, y))

    for string in potential_key_list:
        score += get_string_score(string)

    if (score != 0):
        s.found_pattern = True

    return score