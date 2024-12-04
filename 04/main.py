def find_word(word_search, x, y, dir, letter, check) -> bool:
    if 0 <= x < len(word_search) and 0 <= y < len(word_search[0]):
        if word_search[x][y] == letter:
            print(word_search[x][y], letter)
            if letter == "S":
                for i in range(4):
                    check[x][y] = "SAMX"[i]
                    x -= dir[0]
                    y -= dir[1]
                return True
            x += dir[0]
            y += dir[1]
            letter = "XMAS"["XMAS".index(letter) + 1]
            return find_word(word_search, x, y, dir, letter, check)
    return False


def find_x_mas(word_search, x, y, check) -> bool:
    if not (0 < x < len(word_search) - 1 and 0 < y < len(word_search[0]) - 1):
        return False
    print(x, y)
    pairs_dict = {(1, 1): (-1, -1), (1, -1): (-1, 1)}
    for key in pairs_dict.keys():
        set = {"M", "S"}
        j, k = x + key[0], y + key[1]
        l, m = x + pairs_dict[key][0], y + pairs_dict[key][1]
        if word_search[j][k] not in set:
            return False
        set.remove(word_search[j][k])
        if word_search[l][m] not in set:
            return False
    check[x][y] = "A"
    for key, value in pairs_dict.items():
        check[x + key[0]][y + key[1]] = word_search[x + key[0]][y + key[1]]
        check[x + value[0]][y + value[1]] = word_search[x + value[0]][y + value[1]]
    return True


def main():
    file = "inputs.txt"
    word_search = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            word_search.append(line.strip())
    xmas_count = 0
    check = [["." for i in range(len(word_search[0]))] for j in range(len(word_search))]
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == "X":
                for dir in [
                    (1, 0),
                    (0, 1),
                    (-1, 0),
                    (0, -1),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]:
                    if find_word(word_search, i, j, dir, "X", check):
                        xmas_count += 1
    x_mas_count = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == "A":
                print(i, j)
                if find_x_mas(word_search, i, j, check):
                    x_mas_count += 1

    for line in check:
        print(line)
    print("XMAS count: ", xmas_count)
    print("'X' MAS count: ", x_mas_count)


if __name__ == "__main__":
    main()
