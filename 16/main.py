from collections import defaultdict


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
        stack = [(start, 3, 0, [start])]
        seen = {}
        while stack:
            node, facing, score, path = stack.pop()
            if score > 99448:
                continue
            state = (node, facing)
            if state in seen and seen[state] < score:
                continue
            seen[state] = score
            if node == end:
                print("found {} paths".format(len(paths) + 1))
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
    visited = set()
    for path, score in zip(paths, scores):
        if score == min_score:
            for i in range(len(path) - 1):
                node = path[i]
                next_node = path[i + 1]
                visits = [
                    (x, y)
                    for x in range(
                        min(node[0], next_node[0]),
                        max(node[0], next_node[0]) + 1,
                    )
                    for y in range(
                        min(node[1], next_node[1]),
                        max(node[1], next_node[1]) + 1,
                    )
                ]
                for visit in visits:
                    visited.add(visit)
    print(len(visited))


if __name__ == "__main__":
    main()
