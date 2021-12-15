import itertools


def read_input(file):
    with open(file, "r") as f:
        arr = [line.strip().split(" | ") for line in f.readlines()]
        return arr


def solution_1(arr):
    amount = 0
    for entry in arr:
        display = entry[1].split()
        amount += sum(1 if len(_) in [2, 3, 4, 7] else 0 for _ in display)
    return amount


class Mappings:
    def __init__(self):
        self.digits = {
            0: {1, 2, 3, 5, 6, 7},
            1: {3, 6},
            2: {1, 3, 4, 5, 7},
            3: {1, 3, 4, 6, 7},
            4: {2, 3, 4, 6},
            5: {1, 2, 4, 6, 7},
            6: {1, 2, 4, 5, 6, 7},
            7: {1, 3, 6},
            8: {1, 2, 3, 4, 5, 6, 7},
            9: {1, 2, 3, 4, 6, 7}
        }

        self.possible_letter_mappings = {
            "a": {i for i in range(1, 8)},
            "b": {i for i in range(1, 8)},
            "c": {i for i in range(1, 8)},
            "d": {i for i in range(1, 8)},
            "e": {i for i in range(1, 8)},
            "f": {i for i in range(1, 8)},
            "g": {i for i in range(1, 8)},
        }
        # self.letter_mappings = {
        #     "a": 0,
        #     "b": 0,
        #     "c": 0,
        #     "d": 0,
        #     "e": 0,
        #     "f": 0,
        #     "g": 0,
        # }
    
    def complement(self, digit):
        return {i for i in range(1, 8)} - self.digits[digit]

    def analyze(self, pattern):
        letters = {"a", "b", "c", "d", "e", "f", "g"}
        uniques = {2: 1, 3: 7, 4: 4}
        other_letters = letters - set(pattern)
        if len(pattern) in uniques:
            for letter in pattern:
                self.possible_letter_mappings[letter] = self.possible_letter_mappings[letter] - self.complement(uniques[len(pattern)])
            for letter in other_letters:
                self.possible_letter_mappings[letter] = self.possible_letter_mappings[letter] - self.digits[uniques[len(pattern)]]

    def possibilities(self):
        possibilities = [i for i in itertools.product(*(self.possible_letter_mappings.values())) if len(i) == len(set(i))]
        return possibilities

    def validate(self, pattern, pos):
        self.letter_mappings = dict(zip(["a", "b", "c", "d", "e", "f", "g"], pos))
        res = {self.letter_mappings[k] for k in pattern}
        if res in self.digits.values():
            return res
        return False

def solution_2(arr):
    amount, winner = 0, None
    for entry in arr:
        mappings = Mappings()
        patterns = entry[0].split()
        for pattern in patterns:
            mappings.analyze(pattern)
        for pos in mappings.possibilities():
            winner, is_possibility = pos, True
            for pattern in patterns:
                if not mappings.validate(pattern, pos):
                    is_possibility = False
            if is_possibility:
                break

        display_digits = list()
        for digit in entry[1].split():
            res = mappings.validate(digit, winner)
            assert res
            for k, v in mappings.digits.items():
                if v == res:
                    display_digits.append(str(k))
        amount += int("".join(display_digits))


    return amount


print(solution_2(read_input("day_8_input.txt")))
