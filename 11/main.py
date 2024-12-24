from math import floor, log10
from collections import defaultdict


def process(nums, cur, end):
    cache = defaultdict(dict)

    def recur(num, cur, end):
        if num in cache and cur in cache[num]:
            return cache[num][cur]
        if cur >= end:
            return 1
        if num == 0:
            res = recur(1, cur + 1, end)
        else:
            digits = floor(log10(num)) + 1
            if digits % 2 == 0:
                nstr = str(num)
                left = int(nstr[: digits // 2])
                right = int(nstr[digits // 2 :])
                res = recur(left, cur + 1, end) + recur(right, cur + 1, end)
            else:
                res = recur(num * 2024, cur + 1, end)
        cache[num][cur] = res
        return res

    return sum(recur(num, cur, end) for num in nums)


def main():
    file = "inputs.txt"
    with open(file) as f:
        line = f.read().strip()
    nums = [int(n) for n in line.split()]
    print(process(nums, 0, 75))
    pass


if __name__ == "__main__":
    main()
