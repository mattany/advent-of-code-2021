import copy
from collections import defaultdict
from timeit import default_timer as timer
from datetime import timedelta


class Rule:
    def __init__(self, state, res):
        self.l = state[0]
        self.r = state[1]
        self.m = res
        self.stage = 1

    def __repr__(self):
        return f"{self.l}{self.r} -> {self.m}"


def read_input(file):
    with open(file, "r") as f:
        state = f.readline().strip()
        f.readline()
        rules = {line.strip().split(" -> ")[0]: Rule(*(line.strip().split(" -> "))) for line in f.readlines()}
        return state, rules

def solution_1(state, rules, iterations=10):
    pairs = defaultdict(lambda: 0)
    chars = defaultdict(lambda: 0)

    for i, c in enumerate(state[:-1]):
        pairs[f"{c}{state[i + 1]}"] += 1
        chars[c] += 1
    chars[state[-1]] += 1

    for i in range(iterations):
        new_pairs = defaultdict(lambda: 0)
        for p in pairs.keys():
            print(len(pairs), p, pairs[p])
            np_1, np_2 = f"{rules[p].l}{rules[p].m}", f"{rules[p].m}{rules[p].r}"
            new_pairs[np_1] += pairs[p]
            new_pairs[np_2] += pairs[p]
            chars[rules[p].m] += pairs[p]
        pairs = copy.deepcopy(new_pairs)
    print(chars)
    return max(chars.values()) - min(chars.values())


print(solution_1(*read_input("day_14_input.txt"), 40))