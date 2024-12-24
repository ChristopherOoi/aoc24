def main():
    file = "inputs.txt"
    safe = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = [int(i) for i in line.strip().split()]
            for i in range(len(line)):
                temp = line.copy()
                temp.pop(i)
                sign = 1 if temp[0] < temp[1] else -1
                distances = [temp[i + 1] - temp[i] for i in range(len(temp) - 1)]
                if all(i * sign > 0 for i in distances) and all(
                    0 < abs(i) < 4 for i in distances
                ):
                    safe.append(temp)
                    break
    print(len(safe))


if __name__ == "__main__":
    main()
