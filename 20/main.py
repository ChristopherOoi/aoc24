from collections import defaultdict
from copy import deepcopy


def get_path(lines, s, e):
    x, y = s
    coords = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while True:
        if (x, y) == e:
            coords.append((x, y))
            break
        for dx, dy in directions:
            if lines[x + dx][y + dy] in "E." and (x + dx, y + dy) not in coords:
                coords.append((x, y))
                x += dx
                y += dy
                break
    return coords


def get_cheats(coords, lines, n, threshold):
    cheats = defaultdict(list)
    for i, _ in enumerate(coords):
        for j in range(len(coords) - 1, i + 1, -1):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dist_x = abs(x1 - x2)
            dist_y = abs(y1 - y2)
            if dist_x + dist_y <= n and j - i - dist_x - dist_y >= threshold:
                _x = sorted([x1, x2])
                _y = sorted([y1, y2])
                _x[1] += 1 if x1 == x2 else 0
                _y[1] += 1 if y1 == y2 else 0
                cheat = 0
                xcoords = range(_x[0], _x[1])
                ycoords = range(_y[0], _y[1])
                if any(lines[dx][dy] == "#" for dx in xcoords for dy in _y):
                    cheat = 1
                if any(lines[dx][dy] == "#" for dx in _x for dy in ycoords):
                    cheat = 1
                if cheat:
                    cheats[i].append((j, dist_x + dist_y))
    return cheats


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    for i, line in enumerate(lines):
        if "S" in line:
            s = (i, line.index("S"))
        if "E" in line:
            e = (i, line.index("E"))
    coords = get_path(lines, s, e)
    cheats = get_cheats(coords, lines, 20, 100)
    saved = defaultdict(int)
    for k, v in cheats.items():
        for _v in v:
            saved[_v[0] - k - _v[1]] += 1
    print(saved)
    print(sum(len(v) for v in cheats.values()))


if __name__ == "__main__":
    main()
