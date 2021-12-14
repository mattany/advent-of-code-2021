import util

arr = util.read_input("day_3_input.txt")

def solution_a(arr):
    digit_sums = [0 for _ in range(len(arr[0]))]

    for val in arr:
        for i, digit in enumerate(val):
            if digit == "1":
                digit_sums[i] += 1

    res = []
    for d in digit_sums:
        if d > len(arr) / 2:
            res.append(True)
        else:
            res.append(False)
    return int("0b" + "".join(["1" if i else "0" for i in res]), 2) * int("0b" + "".join(["0" if i else "1" for i in res]), 2)

def solution_b(arr):
    pos = 0
    oxygen_arr, c02scrubber_arr = arr, arr
    while len(oxygen_arr) > 1 or len(c02scrubber_arr) > 1:
        oxygen_zero_arr, oxygen_one_arr = [_ for _ in oxygen_arr if _[pos] == "0"], [_ for _ in oxygen_arr if _[pos] == "1"]
        oxygen_arr = oxygen_one_arr if len(oxygen_one_arr) >= len(oxygen_zero_arr) else oxygen_zero_arr
        c02_zero_arr, c02_one_arr = [_ for _ in c02scrubber_arr if _[pos] == "0"], [_ for _ in c02scrubber_arr if _[pos] == "1"]
        c02scrubber_arr = c02_one_arr if 0 < len(c02_one_arr) < len(c02_zero_arr) or len(c02_zero_arr) == 0 else c02_zero_arr
        pos += 1
    return int(f"0b{oxygen_arr[0]}", 2) * int(f"0b{c02scrubber_arr[0]}", 2)

print(solution_b(arr))