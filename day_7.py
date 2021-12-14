from numpy import inf


def read_input(file):
    with open(file, "r") as f:
        crabs = [int(i) for i in f.readline().strip().split(',')]
    return crabs


def abs_diff(x, y):
    return abs(x - y)


def distances(crabs):
    return {k: sum(_ + 1 for _ in range(k)) for k in range(max(crabs) - min(crabs) + 1)}


def solution_1(crabs, cost_func):
    min_cost = inf
    for i in crabs:
        i_cost = sum(cost_func(_, i) for _ in crabs)
        if i_cost < min_cost:
            min_cost = i_cost
    return min_cost


def solution_2(crabs):
    dist_map = distances(crabs)
    min_cost = inf
    max_crab = max(crabs)
    for i in range(max_crab + 1):
        i_cost = sum(dist_map[abs_diff(_, i)] for _ in crabs)
        if i_cost < min_cost:
            min_cost = i_cost
    return min_cost

# print(growing_diff(2,5))
print(solution_2(read_input("day_7_input.txt")))
