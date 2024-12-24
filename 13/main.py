from collections import defaultdict


def attempt(configs):
    total = 0
    history = defaultdict(dict)
    for config in configs:
        x = [int(l[l.find("X") + 2 : l.find(",")]) for l in config]
        y = [int(l[l.find("Y") + 2 :]) for l in config]
        minimum = 0
        x1, x2, x3 = x
        y1, y2, y3 = y
        x3 += 10000000000000
        y3 += 10000000000000
        if (x1 * y2 - x2 * y1) == 0:
            print("dammit")
        else:
            a_presses = (y2 * x3 - x2 * y3) / (x1 * y2 - x2 * y1)
            b_presses = (-1 * y1 * x3 + x1 * y3) / (x1 * y2 - x2 * y1)
            if int(a_presses) == a_presses and int(b_presses) == b_presses:
                minimum += 3 * a_presses + 1 * b_presses
        history[(x1, x2, y1, y2)][(x3, y3)] = minimum
        total += minimum
    print(total)


def main():
    file = "inputs.txt"
    with open(file, "r") as f:
        lines = [l.strip() for l in f.readlines()]
    configs = [lines[i : i + 3] for i in range(0, len(lines), 4)]
    attempt(configs)
    pass


if __name__ == "__main__":
    main()
