from collections import defaultdict


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = [int(f.strip()) for f in f.readlines()]
    num = 0
    bananas = defaultdict(int)
    for sec in lines:
        change = []
        seen = set()
        for _ in range(2000):
            p = sec
            sec = ((sec << 6) ^ sec) & 0xFFFFFF
            sec = ((sec >> 5) ^ sec) & 0xFFFFFF
            sec = ((sec << 11) ^ sec) & 0xFFFFFF
            change.append(sec % 10 - p % 10)
            if len(change) > 3:
                seq = tuple(change)
                if seq not in seen:
                    bananas[seq] += sec % 10
                    seen.add(seq)
                change = change[1:]
        num += sec
    print(num)
    print(max(bananas.values()))


if __name__ == "__main__":
    main()
