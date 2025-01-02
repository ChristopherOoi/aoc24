import functools


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    nkeypad = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
        "gap": (3, 0),
    }
    rkeypad = {
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2),
        "gap": (0, 0),
    }

    @functools.lru_cache(maxsize=None)
    def get_moves(string, depth, key="n"):

        def get_sequence(cur, nxt, key="n"):
            keypad = nkeypad if key == "n" else rkeypad
            cur_x, cur_y = keypad[cur]
            nxt_x, nxt_y = keypad[nxt]
            dx = nxt_x - cur_x
            dy = nxt_y - cur_y
            cx = "v" if dx > 0 else "^"
            cy = ">" if dy > 0 else "<"
            if cur_x == keypad["gap"][0] and nxt_y == keypad["gap"][1]:
                return [cx * abs(dx) + cy * abs(dy) + "A"]
            if cur_y == keypad["gap"][1] and nxt_x == keypad["gap"][0]:
                return [cy * abs(dy) + cx * abs(dx) + "A"]
            pos = set()
            pos.add(cy * abs(dy) + cx * abs(dx) + "A")
            pos.add(cx * abs(dx) + cy * abs(dy) + "A")
            return list(pos)

        length = 0
        for i in range(len(string) - 1):
            cur = string[i]
            nxt = string[i + 1]
            pos = get_sequence(cur, nxt, key)
            if depth > 1:
                length += min([get_moves("A" + p, depth - 1, "r") for p in pos])
            else:
                length += len(min(pos, key=len))
        return length

    complexity = 0
    for line in lines:
        depth = 26
        string = "A" + line
        res = get_moves(string, depth, "n")
        complexity += res * int(line[:-1])
    print(complexity)


if __name__ == "__main__":
    main()
