import util


def solution_1(arr):
    dirs = [0, 0]
    vertical, horizontal = 0, 1
    for elem in arr:
        direction, amt = elem.split()
        amt = int(amt)

        def down(v=dirs, x=amt):
            v[vertical] += x

        def up(v=dirs, x=amt):
            v[vertical] -= x

        def forward(v=dirs, x=amt):
            v[horizontal] += x

        funcs = {
            "forward": forward,
            "down": down,
            "up": up
        }

        funcs[direction]()

    return dirs[0] * dirs[1]


def solution_2(arr):
    dirs = [0, 0, 0]
    vertical, horizontal, aim = 0, 1, 2
    for elem in arr:
        direction, amt = elem.split()
        amt = int(amt)

        def down(v=dirs, x=amt):
            v[aim] += x

        def up(v=dirs, x=amt):
            v[aim] -= x

        def forward(v=dirs, x=amt):
            v[horizontal] += x
            v[vertical] += x * v[aim]

        funcs = {
            "forward": forward,
            "down": down,
            "up": up
        }

        funcs[direction]()

    return dirs[vertical] * dirs[horizontal]
