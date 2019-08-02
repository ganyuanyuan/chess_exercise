import random

class  Engine(object):

    def __init__(self, chessboard):
        self.__chessboard = chessboard


    def parse_user_input(self, input, chessman):
        res = input.split(',')
        pos_x = int(res[0])
        pos_y = int(res[1])
        chessman.set_position((pos_x, pos_y))

    def computer_go(self, chessman):
        while True:
            pos_x = random.randint(0,4)
            pos_y = random.randint(0,4)
            if self.__chessboard.get_chess((pos_x,pos_y))=='_':
                print('computer go:', pos_x, pos_y)
                chessman.set_position((pos_x,pos_y))
                break

    def is_won(self, pos, color):
        count = 0
        for pos_x in range(5):
            if self.__chessboard.get_chess((pos_x,pos[1])) == color:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 0

        count = 0
        for pos_y in range(5):
            if self.__chessboard.get_chess((pos[0], pos_y)) == color:
                count+= 1
                if count >=3:
                    return True
            else:
                count = 0

        return False

    def is_wonman(self,chessman):
        pos = chessman.get_position()
        color = chessman.get_color()
        return self.is_won(pos, color)
