class Chessboard(object):
    board_size = 5

    def __init__(self):
        self.__board = [[0 for _ in range(Chessboard.board_size)] for _ in range(Chessboard.board_size)]

    def init_board(self):
        for i in range(Chessboard.board_size):
            for j in range(Chessboard.board_size):
                self.__board[i][j] = '_'

    def print_board(self):
        for i in range(Chessboard.board_size):
            print(self.__board[i])


    def set_chess(self, pos, color):
        self.__board[pos[0]][pos[1]] = color

    def set_chessman(self, chessman):
        pos = chessman.get_position()
        color = chessman.get_color()
        self.set_chess(pos, color)

    def get_chess(self, pos):
        return self.__board[pos[0]][pos[1]]
