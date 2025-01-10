def main():
    with open("inputs.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    locks = []
    keys = []
    while lines:
        schematic, lines = lines[:7], lines[8:]
        schematic = list(zip(*schematic))
        count = [l.count("#") - 1 for l in schematic]
        if schematic[0][0] == "#":
            locks.append(count)
        else:
            keys.append(count)
    count = 0
    for lock in locks:
        for key in keys:
            if any(l + k > 5 for l, k in zip(lock, key)):
                continue
            else:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
