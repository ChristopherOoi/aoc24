from copy import deepcopy


def make_grid(bound, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    junctions = [(0, 0, 0, directions)]
    while junctions:
        _x, _y, cost, dirs = junctions.pop(0)
        for dx, dy in dirs:
            new_cost = cost + 1
            x, y = _x + dx, _y + dy
            while 0 <= x <= bound and 0 <= y <= bound and grid[x][y] != -1:
                if grid[x][y] == 0 or grid[x][y] > new_cost:
                    grid[x][y] = new_cost
                else:
                    break
                temp_dirs = [
                    (j, k)
                    for j, k in directions
                    if abs(j) != abs(dx)
                    and abs(k) != abs(dy)
                    and 0 <= x + j <= bound
                    and 0 <= y + k <= bound
                ]
                new_directions = []
                for j, k in temp_dirs:
                    if grid[x + j][y + k] == 0 or grid[x + j][y + k] > new_cost:
                        new_directions.append((j, k))
                if len(new_directions):
                    junctions.append((x, y, new_cost, new_directions))
                new_cost += 1
                x, y = x + dx, y + dy
    return grid


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
    bound = 70
    grid = [[0 for _ in range(bound + 1)] for _ in range(bound + 1)]
    for i in range(12, len(lines) + 1):
        temp = deepcopy(grid)
        for line in lines[:i]:
            y, x = [int(n) for n in line.split(",")]
            temp[x][y] = -1
        temp = make_grid(bound, temp)
        if temp[bound][bound] < 1:
            print(i - 1)
            print(lines[i - 1])
            break


if __name__ == "__main__":
    main()
