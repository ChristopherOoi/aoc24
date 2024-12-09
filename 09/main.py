from copy import deepcopy


def get_blocks(line):
    disk = []
    empty = []
    for i in range(0, len(line)):
        if i % 2 == 0:
            disk.append(int(line[i]))
        else:
            empty.append(int(line[i]))
    return disk, empty


def move_blocks(disk, empty):
    moved = []
    maximum = len(disk) - 1
    item = 0
    while empty and disk:
        num = disk.pop(0)
        for _ in range(num):
            moved.append(item)
        item += 1
        to_move = empty.pop(0)
        while to_move > 0 and disk:
            moved.append(maximum)
            to_move -= 1
            disk[-1] -= 1
            if disk[-1] == 0:
                disk = disk[:-1]
                maximum -= 1
    return moved


def move_blocks_better(line, disk):
    moved = []
    data = []
    count = 0
    for i, n in enumerate(disk):
        start = sum([int(x) for x in line[: i * 2]])
        length = n
        data.append([start, length, i, 0])
    j = len(data) - 1
    while j > 0:
        print(j)
        if data[j][3] == 1:
            j -= 1
            continue
        for i in range(1, j + 1):
            gap = data[i][0] - data[i - 1][0] - data[i - 1][1]
            if gap >= data[j][1]:
                data[j][0] = data[i - 1][0] + data[i - 1][1]
                data[j][3] = 1
                data = sorted(data, key=lambda x: x[0])
                count += 1
                break
        else:
            j -= 1
    for i in range(len(data)):
        cur_start = data[i][0]
        cur_length = data[i][1]
        cur_index = data[i][2]
        next_start = data[i + 1][0] if i < len(data) - 1 else 0
        for _ in range(cur_length):
            moved.append(cur_index)
        if next_start and next_start - cur_start - cur_length > 0:
            for _ in range(next_start - cur_start - cur_length):
                moved.append(".")
    print(count)
    return moved


def main():
    file = "inputs.txt"
    with open(file) as f:
        line = f.read().strip()
    disk, empty = get_blocks(line)
    moved = move_blocks(deepcopy(disk), deepcopy(empty))
    checksum = 0
    for i, c in enumerate(moved):
        if c == ".":
            break
        checksum += i * c
    print("Checksum: ", checksum)
    moved = move_blocks_better(line, deepcopy(disk))
    checksum = 0
    for i, c in enumerate(moved):
        if c == ".":
            continue
        checksum += i * c
    print("Checksum: ", checksum)


if __name__ == "__main__":
    main()
