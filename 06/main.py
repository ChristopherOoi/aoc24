from time import sleep
from copy import deepcopy


def traverse(lab_map, pos):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    marks = ["|", "-"]
    diri = 0
    distinct_positions = 0
    temp_map = [[0 for _ in range(len(lab_map[0]))] for _ in range(len(lab_map))]
    while True:
        inc_x, inc_y = dirs[diri]
        if lab_map[pos[0]][pos[1]] not in "|-+":
            distinct_positions += 1
        mark = diri % 2
        if lab_map[pos[0]][pos[1]] == "." or lab_map[pos[0]][pos[1]] == "^":
            lab_map[pos[0]][pos[1]] = marks[mark]
        elif lab_map[pos[0]][pos[1]] != marks[mark]:
            lab_map[pos[0]][pos[1]] = "+"
        temp_map[pos[0]][pos[1]] += 1
        if temp_map[pos[0]][pos[1]] > 5:
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
    for x in range(len(new_map)):
        for y in range(len(new_map[0])):
            temp_map = deepcopy(lab_map)
            check = []
            if 0 < x:
                check.append(new_map[x - 1][y])
            if x < len(new_map) - 1:
                check.append(new_map[x + 1][y])
            if 0 < y:
                check.append(new_map[x][y - 1])
            if y < len(new_map[0]) - 1:
                check.append(new_map[x][y + 1])
            if not any(c in "|-+" for c in check):
                continue
            if temp_map[x][y] == ".":
                temp_map[x][y] = "#"
                distinct, _ = traverse(temp_map, pos)
                if distinct == 0:
                    obstacles += 1
    return obstacles


def main():
    file = "inputs.txt"
    lab_map = []
    position = (0, 0)
    with open(file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "^" in line:
                position = (i, line.index("^"))
            lab_map.append(list(line.strip()))
    temp_map = deepcopy(lab_map)
    distinct, new_map = traverse(temp_map, position)
    print("Distinct: ", distinct)
    obstacles = obstruct(new_map, lab_map, position)
    print("Obstacles: ", obstacles)


if __name__ == "__main__":
    main()
