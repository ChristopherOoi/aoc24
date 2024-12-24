from collections import defaultdict


def get_region(lines):
    visited = set()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def traverse(lines, x, y, c, region) -> int:
        if not 0 <= x < len(lines) or not 0 <= y < len(lines[x]) or lines[x][y] != c:
            return 1
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        pts.add((x, y))
        per = 0
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]
            per += traverse(lines, nx, ny, c, region)
        region.append(per)
        return 0

    def get_lines(pts):
        hor = defaultdict(list)
        ver = defaultdict(list)
        for x, y in pts:
            hor[x].append(y)
            ver[y].append(x)
        x_min, y_min = (
            min(min(v) for v in hor.values()),
            min(min(v) for v in ver.values()),
        )
        hor = {k: sorted(v) for k, v in hor.items()}
        ver = {k: sorted(v) for k, v in ver.items()}
        for k, vs in hor.items():
            hor[k] = [x - x_min for x in vs]
        for k, vs in ver.items():
            ver[k] = [y - y_min for y in vs]
        return (
            dict(sorted(hor.items())),
            dict(sorted(ver.items())),
        )

    def get_ends(perspective):
        values = perspective.values()
        starts = []
        ends = []
        s = 1
        e = 1
        for i, val in enumerate(values):
            tstarts = [val[0]]
            tends = []
            for j in range(1, len(val)):
                if val[j] - val[j - 1] != 1:
                    tends.append(val[j - 1])
                    tstarts.append(val[j])
            tends.append(val[-1])
            if i == 0:
                s = len(tstarts)
                e = len(tends)
            elif i != 0:
                for start in tstarts:
                    if start not in starts:
                        s += 1
                for end in tends:
                    if end not in ends:
                        e += 1
            starts = tstarts
            ends = tends
        return s + e

    price = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i, j) not in visited:
                region = []
                pts = set()
                traverse(lines, i, j, lines[i][j], region)
                hor, ver = get_lines(pts)
                side = 0
                side += get_ends(hor)
                side += get_ends(ver)
                print(len(region) * side)
                print(len(region), side)
                price += len(region) * side
    print(price)


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [l.strip() for l in f.readlines()]
    get_region(lines)
    pass


if __name__ == "__main__":
    main()
