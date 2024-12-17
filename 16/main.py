from collections import defaultdict


def find_paths(start, end, nodes, directions):
    paths = []
    queue = [(start, [start])]
    while queue:
        current, path = queue.pop(0)
        if current == end:
            paths.append(path)
        for node in nodes[current]:
            if node not in path:
                queue.append((node, path + [node]))
    return paths


def main():
    file = "inputs.txt"
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    with open(file) as f:
        lines = f.readlines()
        corners = []
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == "S":
                    start = (i, j)
                    corners.append((i, j))
                elif c == "E":
                    end = (i, j)
                    corners.append((i, j))
                if 0 < i < len(lines) - 1 and 0 < j < len(line) - 1 and c in "SE.":
                    dirs = [lines[i + x][j + y] in "SE." for x, y in directions]
                    if any(sum(dirs[g : g + 2]) >= 2 for g in range(len(dirs))):
                        corners.append((i, j))
    nodes = defaultdict(set)
    for corner in corners:
        lines[corner[0]] = (
            lines[corner[0]][: corner[1]] + "X" + lines[corner[0]][corner[1] + 1 :]
        )
        i, j = corner
        for direction in directions:
            x, y = i, j
            while 0 < x < len(lines) - 1 and 0 < y < len(lines[0]) - 1:
                x += direction[0]
                y += direction[1]
                if lines[x][y] == "#":
                    break
                if (x, y) in corners:
                    nodes[(x, y)].add((i, j))
                    break
    print(len(nodes))

    def find_all_paths(nodes, start, end, directions):
        paths = []
        scores = []
        seen = {}
        stack = [(start, 3, 0, [start])]
        while stack:
            node, facing, score, path = stack.pop()
            state = (node, facing)
            if state in seen and seen[state] <= score:
                continue
            seen[state] = score
            if node == end:
                paths.append(path)
                scores.append(score)
                continue
            for next_node in nodes[node]:
                if next_node not in path:
                    dx = next_node[0] - node[0]
                    dy = next_node[1] - node[1]
                    distance = abs(dx) + abs(dy)
                    new_facing = directions.index((dx / distance, dy / distance))
                    turn_cost = (
                        min(abs(new_facing - facing), 4 - abs(new_facing - facing))
                        * 1000
                    )
                    new_score = score + distance + turn_cost
                    new_path = path + [next_node]
                    stack.append((next_node, new_facing, new_score, new_path))

        return paths, scores

    paths, scores = find_all_paths(nodes, start, end, directions)
    min_score = min(scores)
    print(min_score)


if __name__ == "__main__":
    main()
