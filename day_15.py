from functools import total_ordering

import numpy as np
import heapq
from functools import total_ordering
from timeit import default_timer as timer
from datetime import timedelta




dist = np.ndarray


@total_ordering
class Vertex:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def distance(self):
        return dist[self.i, self.j]

    def __repr__(self):
        return f"distance: {self.distance()}, i: {self.i}, j: {self.j}"

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()


def read_input(file):
    with open(file, "r") as f:
        arr = [list(line.strip()) for line in f.readlines()]
        for i, line in enumerate(arr):
            arr[i] = [int(_) for _ in line]
    return arr


def solution_1(arr):
    global dist
    dim = len(arr)
    prev = [[(-1, -1) for j in range(dim)] for i in range(dim)]
    prev = np.array(prev, dtype="i,i")
    risks = arr
    dist = np.empty([dim, dim])
    dist.fill(np.inf)
    dist[0, 0] = 0
    q = [Vertex(i, j) for i in range(dim) for j in range(dim)]
    heapq.heapify(q)
    cur = (0, 0)
    # some vertices remain to be visited
    start = timer()

    while len(q):
        if len(q) % ((dim*dim) / 10000) == 0:
            frac = ((dim * dim - len(q)) / (dim * dim))
            print(frac * 100, "%. remaining: ", len(q))
            end = timer()
            delta = timedelta(seconds=end - start)
            if (frac):
                print("elapsed: ", delta, "ETA: ", (delta * (1 / frac)) - delta)
                print()
        u = heapq.heappop(q)
        neighbors = []
        i, j = u.i, u.j
        if i > 0:
            neighbors.append((i - 1, j))
        if i < dim - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < dim - 1:
            neighbors.append((i, j + 1))

        i, j = 0, 1
        for v in neighbors:
            alt = u.distance() + risks[v[i], v[j]]
            if alt < dist[v[i], v[j]]:
                dist[v[i], v[j]] = alt
                prev[v[i], v[j]] = (u.i, u.j)
        heapq.heapify(q)

    return dist[dim - 1, dim - 1]
    # vertices = [[Vertex(_) for _ in row] for row in arr]
    # edges = set()
    # for i in range(len(vertices)):
    #     for j in range(len(vertices[0])):
    #         v = vertices[i][j]

    #

def f(x):
    ret = x + 1
    if ret == 10:
        ret = 1
    return ret

def solution_2(arr: np.ndarray):
    arrs = [arr]
    for i in range(8):
        arrs.append(np.frompyfunc(f, 1, 1)(arrs[-1]))
    row_0 = np.concatenate((arrs[0], arrs[1]), axis=1)
    row_0 = np.concatenate((row_0, arrs[2]), axis=1)
    row_0 = np.concatenate((row_0, arrs[3]), axis=1)
    row_0 = np.concatenate((row_0, arrs[4]), axis=1)

    row_1 = np.concatenate((arrs[1], arrs[2]), axis=1)
    row_1 = np.concatenate((row_1, arrs[3]), axis=1)
    row_1 = np.concatenate((row_1, arrs[4]), axis=1)
    row_1 = np.concatenate((row_1, arrs[5]), axis=1)

    row_2 = np.concatenate((arrs[2], arrs[3]), axis=1)
    row_2 = np.concatenate((row_2, arrs[4]), axis=1)
    row_2 = np.concatenate((row_2, arrs[5]), axis=1)
    row_2 = np.concatenate((row_2, arrs[6]), axis=1)

    row_3 = np.concatenate((arrs[3], arrs[4]), axis=1)
    row_3 = np.concatenate((row_3, arrs[5]), axis=1)
    row_3 = np.concatenate((row_3, arrs[6]), axis=1)
    row_3 = np.concatenate((row_3, arrs[7]), axis=1)

    row_4 = np.concatenate((arrs[4], arrs[5]), axis=1)
    row_4 = np.concatenate((row_4, arrs[6]), axis=1)
    row_4 = np.concatenate((row_4, arrs[7]), axis=1)
    row_4 = np.concatenate((row_4, arrs[8]), axis=1)

    mat = np.concatenate((row_0, row_1, row_2, row_3, row_4), axis=0)

    return solution_1(mat)

print(solution_2(np.array(read_input("day_15_input.txt"))))
