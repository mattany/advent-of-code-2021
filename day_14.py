class Rule:
    def __init__(self, state, res):
        self.left = state[0]
        self.right = state[1]
        self.res = res

    def __repr__(self):
        return f"{self.left}{self.right} -> {self.res}"


def read_input(file):
    with open(file, "r") as f:
        state = f.readline().strip()
        f.readline()
        rules = {line.strip().split(" -> ")[0]: Rule(*(line.strip().split(" -> "))) for line in f.readlines()}
        return state, rules


def apply_rules(rules, state):
    new_letters = ["" for _ in range(len(state) - 1)]
    for i, letter in enumerate(state[:-1]):
        if f"{letter}{state[i + 1]}" in rules:
            new_letters[i] = rules[f"{letter}{state[i + 1]}"].res
    new_state = []
    for i in range(len(state) - 1):
        new_state.append(state[i])
        new_state.append(new_letters[i])
    new_state.append(state[-1])
    return "".join(new_state)


def solution_1(state, rules, iterations=10):
    for i in range(iterations):
        print(i)
        state = apply_rules(rules, state)
    counts = dict()
    while state:
        letter = state[0]
        counts[letter] = state.count(letter)
        state = state.replace(letter, "")
    max_val, min_val = max(counts.values()), min(counts.values())
    return max_val - min_val


def solution_2(state, rules):
    return solution_1(state, rules, iterations=40)

print(solution_2(*read_input("day_14_input.txt")))
