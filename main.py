from chessman import *
from chessboard import *
from engine import *
import time

def main():
    chessboard= Chessboard()
    chessboard.init_board()
    chessboard.print_board()
    engine = Engine(chessboard)

    count = 0
    while True:
        chessman = Chessman()
        chessman.set_color('X')
        i = input('format: x, y\n')
        if i == 'stop':
            break
        engine.parse_user_input(i, chessman)

        chessboard.set_chessman(chessman)
        count += 1
        chessboard.print_board()
        if engine.is_wonman(chessman):
            print('you won!')
            break

        chessman = Chessman()
        chessman.set_color('O')
        print('computer go...')
        time.sleep(1)
        engine.computer_go(chessman)

        chessboard.set_chessman(chessman)
        count +=1
        time.sleep(1)
        chessboard.print_board()
        if engine.is_wonman(chessman):
            print('computer won!')
            break






if __name__ == '__main__':
    while True:
        print('start!')
        main()
        is_stop = input('stop?\n')
        if is_stop == 'yes':
            break
    print('stop!')
