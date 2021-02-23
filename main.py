#!/usr/bin/python3

import pbrain_commands as cmd

def main():
    while(1):
        try:
            line = input()
            if 'START' in line: cmd.start(line)
            if 'BEGIN' in line: cmd.begin()
            if 'TURN' in line: cmd.turn(line)
            if 'BOARD' in line: cmd.reconfigBoard()
            if 'END' in line: cmd.quit()
            if 'ABOUT' in line: cmd.about()
            if 'DISPLAY' in line: cmd.display()
        except EOFError as e:
            continue

if __name__ == '__main__':
    main()