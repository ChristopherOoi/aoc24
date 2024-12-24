from collections import defaultdict


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


def main():
    file = "input.txt"
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    for i, line in enumerate(lines):
        if "S" in line:
            s = (i, line.index("S"))
        if "E" in line:
            e = (i, line.index("E"))
    print(s, e)
    coords = get_path(lines, s, e)
    print(len(coords))
    print(coords)
    cheats = defaultdict(list)
    for i, coord in enumerate(coords):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            if x1 == x2 and abs(y1 - y2) == 2:
                if any(lines[x1][dy] == "#" for dy in range(min(y1, y2), max(y1, y2))):
                    cheats[i].append(j)
            elif y1 == y2 and abs(x1 - x2) == 2:
                if any(lines[dx][y1] == "#" for dx in range(min(x1, x2), max(x1, x2))):
                    cheats[i].append(j)
    print(cheats)
    print(len(cheats))


if __name__ == "__main__":
    main()
