from functools import lru_cache


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [line.strip() for line in f.readlines() if len(line.strip()) > 0]
    towels = set([t.strip() for t in lines[0].split(",")])
    arrangements = lines[1:]

    @lru_cache(maxsize=None)
    def arrange(arrangement, index):
        if index == len(arrangement):
            return 1
        count = 0
        for towel in towels:
            if arrangement.startswith(towel, index):
                count += arrange(arrangement, index + len(towel))
        return count

    print(sum(arrange(arrangement, 0) for arrangement in arrangements))


if __name__ == "__main__":
    main()
