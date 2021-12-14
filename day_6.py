def read_input(file):
    with open(file, "r") as f:
        fish = [int(i) for i in f.readline().strip().split(',')]
    return fish


def solution_1(inp, iterations=80):
    incubating = [inp.count(_) for _ in range(7)]
    waiting = [0, 0]
    for i in range(iterations):
        hatched = incubating.pop(0)
        started_incubating = waiting.pop(0)
        waiting.append(hatched)
        incubating.append(hatched + started_incubating)
    return sum(incubating + waiting)

def solution_2(inp):
    return solution_1(inp, iterations=256)

inp = read_input("day_6_input.txt")
print(solution_2(inp))