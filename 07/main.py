from operator import add, mul
from itertools import product


def validate(ress, nums):
    ops = ["+", "*", "||"]
    operators = product(ops, repeat=len(nums) - 1)
    for op_list in operators:
        res = nums[0]
        for num, op in zip(nums[1:], op_list):
            if op == "+":
                res = add(res, num)
            elif op == "*":
                res = mul(res, num)
            elif op == "||":
                res = int(str(res) + str(num))
        if res == ress:
            return True
    return False


def main():
    file = "inputs.txt"
    ress = []
    nums = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            l = line.split(":")
            num = l[1].strip().split(" ")
            nums.append([int(n) for n in num])
            res = l[0].strip()
            ress.append(int(res))
    calibration = 0
    for res, num_list in zip(ress, nums):
        if validate(res, num_list):
            calibration += res
    print(calibration)
    pass


if __name__ == "__main__":
    main()
