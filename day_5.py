import numpy as np


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def slope(p1, p2):
    if p1.x == p2.x:
        return np.inf
    return (p2.y - p1.y) / (p2.x - p1.x)


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.slope = slope(p1, p2)
        self.height = self.p1.y - (self.slope * self.p1.x)

    def mark_line(self, diagram: np.ndarray, diagonal=True):
        if self.slope == np.inf:
            diagram[self.p1.x, min(self.p1.y, self.p2.y): max(self.p1.y, self.p2.y) + 1] += 1
        elif self.slope == 0:
            diagram[min(self.p1.x, self.p2.x): max(self.p1.x, self.p2.x) + 1, self.p1.y] += 1
        elif diagonal:
            for i in range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x) + 1):
                j = (self.slope * i) + self.height
                print(f"{int(i)}, {int(j)}, {self.slope}")
                diagram[i, int(j)] += 1


def read_input(file):
    with open(file, "r") as f:
        arr = [line.strip().split(" -> ") for line in f.readlines()]
    for i, elem in enumerate(arr):
        p1, p2 = elem[0].split(','), elem[1].split(',')
        arr[i] = [Point(int(p1[0]), int(p1[1])), Point(int(p2[0]), int(p2[1]))]
    return [Line(_[0], _[1]) for _ in arr]


inputs = read_input("day_5_input.txt")
dim = 1000


def solution_1(lines, diagonal=False):
    diagram = np.zeros([dim, dim])
    for line in lines:
        line.mark_line(diagram, diagonal=diagonal)
    f = lambda x: 0 if x < 2 else 1
    f_arr = np.frompyfunc(f, 1, 1)
    diagram = f_arr(diagram)
    return np.sum(diagram)


def solution_2(lines):
    return solution_1(lines, diagonal=True)
