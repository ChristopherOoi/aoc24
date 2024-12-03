def main():
    file = "inputs.txt"
    total = 0
    with open(file, "r") as f:
        lines = f.readlines()
        lines[0] = "do()" + lines[0]
        lines = "".join(lines).split("do()")
        lines = [l.split("don't()")[0] for l in lines]
        for line in lines:
            strings = line.split("mul(")
            strings = [s.split(")")[0] for s in strings]
            for s in strings:
                nums = s.split(",")
                if (
                    len(nums) == 2
                    and all(4 > len(n) > 0 for n in nums)
                    and all(n.isdigit() for n in nums)
                ):
                    try:
                        a = int(nums[0])
                        b = int(nums[1])
                        total += a * b
                    except ValueError:
                        continue
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
