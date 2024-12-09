from itertools import combinations
from collections import defaultdict


def get_antenna(map_lines):
    antenna = defaultdict(list)
    for i, line in enumerate(map_lines):
        for j, char in enumerate(line):
            if char == ".":
                continue
            antenna[char].append((i, j))
    return antenna


def antinode(map_lines, antennas):
    antinodes = set()
    for char_pos in antennas.values():
        for (x1, y1), (x2, y2) in combinations(char_pos, 2):
            dx = x2 - x1
            dy = y2 - y1
            x, y = x1 - dx, y1 - dy
            if 0 <= x < len(map_lines) and 0 <= y < len(map_lines[0]):
                antinodes.add((x, y))
            x, y = x2 + dx, y2 + dy
            if 0 <= x < len(map_lines) and 0 <= y < len(map_lines[0]):
                antinodes.add((x, y))
    return len(antinodes)


def resonance(map_lines, antennas):
    antinodes = set()
    for char_pos in antennas.values():
        for (x1, y1), (x2, y2) in combinations(char_pos, 2):
            dx = x2 - x1
            dy = y2 - y1
            x, y = x1, y1
            while True:
                if 0 <= x < len(map_lines) and 0 <= y < len(map_lines[0]):
                    antinodes.add((x, y))
                    x -= dx
                    y -= dy
                else:
                    break
            x, y = x2, y2
            while True:
                if 0 <= x < len(map_lines) and 0 <= y < len(map_lines[0]):
                    antinodes.add((x, y))
                    x += dx
                    y += dy
                else:
                    break
    return len(antinodes)


def main():
    file = "inputs.txt"
    map_lines = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            map_lines.append([c for c in line.strip()])
    grid = set()
    for i, line in enumerate(map_lines):
        for j, _ in enumerate(line):
            grid.add((i, j))
    antennas = get_antenna(map_lines)
    print(antinode(map_lines, antennas))
    print(resonance(map_lines, antennas))


if __name__ == "__main__":
    main()
