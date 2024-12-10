def traverse(topo, row, col, prev, paths):
    if not 0 <= row < len(topo) or not 0 <= col < len(topo[0]):
        return 0
    val = int(topo[row][col])
    if val - prev != 1:
        return 0
    if val == 9:
        paths.add((row, col))
        return 1
    return (
        traverse(topo, row + 1, col, val, paths)
        + traverse(topo, row - 1, col, val, paths)
        + traverse(topo, row, col + 1, val, paths)
        + traverse(topo, row, col - 1, val, paths)
    )


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [s.strip() for s in f.readlines()]
    trails = []
    trailscores = []
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "0":
                paths = set()
                trailscores.append(traverse(lines, row, col, -1, paths))
                trails.append(paths)
    count = 0
    for trail in trails:
        count += len(trail)
    print("Trailheads score: ", count)
    print(trailscores)
    print("Trails score: ", sum(trailscores))
    pass


if __name__ == "__main__":
    main()
