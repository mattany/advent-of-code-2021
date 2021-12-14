def read_input(file):
    with open(file, "r") as f:
        arr = [int(line.strip()) for line in f.readlines()]
        return arr


def solution_1(arr):
    cur = arr.pop(0)
    increases = 0
    for elem in arr:
        if elem > cur:
            increases += 1
        cur = elem
    return increases


def solution_2(arr):
    sw = arr[:3]
    increases = 0
    for i, elem in enumerate(arr[3:]):
        sw_prev_sum = sum(sw)
        sw_i = i % 3
        sw[sw_i] = elem
        sw_sum = sum(sw)
        if sw_sum > sw_prev_sum:
            increases += 1
    return increases
