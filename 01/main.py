def main():
    file = "inputs.txt"
    list1 = []
    list2 = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    list1.sort()
    list2.sort()
    # part 1
    print("Distance: ", sum([abs(x - y) for x, y in zip(list1, list2)]))
    # part 2
    similarity = 0
    for item in list1:
        similarity += item * list2.count(item)
    print("Similarity: ", similarity)


if __name__ == "__main__":
    main()
