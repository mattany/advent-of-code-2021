class Board:
    def __init__(self, board):
        self.active = True
        self.win_index = -1
        self.dimension = 5
        self.marked = [[0 for i in range(self.dimension)] for i in range(self.dimension)]
        self.board = board
        self.score = self._score(board)

    def make_move(self, item):
        if self.active:
            i, j = self.locate(item)
            if (i, j) != (-1, -1):
                self.marked[i][j] = 1
                if all(self.marked[i]) or all([self.marked[_][j] for _ in range(self.dimension)]):
                    self.score = self._score(item)
                    self.active = False
                    return True
                return False

    def _score(self, item):
        score = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if not self.marked[i][j]:
                    score += self.board[i][j]
        return score * item

    def locate(self, item):
        for i, row in enumerate(self.board):
            for j, elem in enumerate(row):
                if elem == item:
                    return i, j
        return -1, -1

def read_input(file, draws, boards):
    with open(file, "r") as f:
        draws += [int(i) for i in f.readline().strip().split(',')]
        board = list()
        for i, line in enumerate(f.readlines()):
            if i % 6 == 0:
                boards.append(board)
                board = list()
            else:
                board.append([int(i) for i in line.strip().split()])
        boards.pop(0)


draws, boards = list(), list()
read_input("day_4_input.txt", draws, boards)


def solution_a(draws, boards):
    board_objects = [Board(_) for _ in boards]
    for draw in draws:
        for board in board_objects:
            if board.make_move(draw):
                return board.score()
    return -1

def solution_b(draws, boards):
    board_objects = [Board(_) for _ in boards]
    win_index = 0
    for draw in draws:
        for board in board_objects:
            if board.make_move(draw):
                board.win_index = win_index
                win_index += 1
    return max(board_objects, key=lambda x: x.win_index).score


print(solution_b(draws, boards))
