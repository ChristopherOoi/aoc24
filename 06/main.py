def traverse(lab_map, pos):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    marks = ["|", "-"]
    diri = 0
    distinct_positions = 0
    lab_map[pos[0]][pos[1] - 1] = "#"
    while True:
        inc_x, inc_y = dirs[diri]
        if lab_map[pos[0]][pos[1]] not in "|-+":
            distinct_positions += 1
        mark = diri % 2
        if lab_map[pos[0]][pos[1]] == ".":
            lab_map[pos[0]][pos[1]] = marks[mark]
        elif lab_map[pos[0]][pos[1]] != marks[mark]:
            lab_map[pos[0]][pos[1]] = "+"
        elif lab_map[pos[0]][pos[1]] in "|-+":
            return 0, lab_map
        temp_pos = (pos[0] + inc_x, pos[1] + inc_y)
        if not (0 <= temp_pos[0] < len(lab_map) and 0 <= temp_pos[1] < len(lab_map[0])):
            return distinct_positions, lab_map
        if lab_map[temp_pos[0]][temp_pos[1]] == "#":
            diri = (diri + 1) % 4
            continue
        pos = temp_pos


def obstruct(new_map, lab_map, pos):
    obstacles = 0
    crosses = [
        (x, y)
        for x in range(len(new_map))
        for y in range(len(new_map[0]))
        if new_map[x][y] == "+"
    ]
    print(crosses)
    potential = []
    for i in range(len(crosses)):
        for j in range(i + 1, len(crosses)):
            intersects = []
            x1, y1 = crosses[i]
            x2, y2 = crosses[j]
            if x1 == x2 or y1 == y2:
                continue
            intersects.append((x1, y2))
            intersects.append((x2, y1))
            hors = [new_map[x][min(y1, y2) + 1 : max(y1, y2)] for x in (x1, x2)]
            vers = [
                [new_map[x][y] for x in range(min(x1, x2) + 1, max(x1, x2))]
                for y in (y1, y2)
            ]
            print(x1, y1, x2, y2)
            print("hors ", hors, "vers ", vers)


def main():
    file = "input.txt"
    lab_map = []
    position = (0, 0)
    with open(file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "^" in line:
                position = (i, line.index("^"))
            lab_map.append(list(line.strip()))
    distinct, new_map = traverse(lab_map, position)
    obstruct(new_map, lab_map, position)
    for row in lab_map:
        print("".join(row))
    print("Distinct: ", distinct)


if __name__ == "__main__":
    main()
