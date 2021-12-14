def read_input(file):
    with open(file, "r") as f:
        arr = [line.strip() for line in f.readlines()]
        return arr