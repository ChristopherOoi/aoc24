from time import sleep


def move_robot(robot, boxes, walls, moves):
    move_list = "<>^v"
    x_bound = max([x[0] for x in walls])
    y_bound = max([x[1] for x in walls])
    for m in moves:
        for i in range(0, x_bound + 1):
            for j in range(0, y_bound + 1):
                if [i, j] in boxes:
                    print("O", end="")
                elif [i, j] in walls:
                    print("#", end="")
                elif [i, j] == robot:
                    print("@", end="")
                else:
                    print(".", end="")
            print()
        input()
        temp_x, temp_y = robot[0], robot[1]
        m_index = move_list.index(m)
        if m_index == 0:
            temp_y -= 1
            to_check = [[temp_x, y] for y in range(temp_y, -1, -1)]
        elif m_index == 1:
            temp_y += 1
            to_check = [[temp_x, y] for y in range(temp_y, y_bound + 1)]
        elif m_index == 2:
            temp_x -= 1
            to_check = [[x, temp_y] for x in range(temp_x, -1, -1)]
        elif m_index == 3:
            temp_x += 1
            to_check = [[x, temp_y] for x in range(temp_x, x_bound + 1)]
        box_indexes = []
        for i, spot in enumerate(to_check):
            if spot not in boxes and spot not in walls:
                break
            if spot in boxes:
                box_index = boxes.index(spot)
                if box_index % 2 == 1:
                    box_indexes.append(boxes.index(spot) - 1)
                box_indexes.append(boxes.index(spot))
                if box_index % 2 == 0:
                    box_indexes.append(boxes.index(spot) + 1)
            else:
                box_indexes.append(-1)
                break
        print(robot, m, box_indexes)
        if len(box_indexes) and box_indexes[-1] == -1:
            continue
        robot = [temp_x, temp_y]
        for index in set(box_indexes):
            if m_index == 0:
                boxes[index][1] -= 1
            elif m_index == 1:
                boxes[index][1] += 1
            elif m_index == 2:
                boxes[index][0] -= 1
            elif m_index == 3:
                boxes[index][0] += 1
    gps = 0
    for box in boxes[::2]:
        print(box)
        gps += box[0] * 100 + box[1]
    print(gps)


def move_robot2(robot, boxes, walls, moves):
    move_list = "<>^v"
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    for m in moves:
        #        for i in range(0, x_bound + 1):
        #            j = 0
        #            while j < y_bound + 1:
        #                if [i, j] in boxes:
        #                    print("[]", end="")
        #                    j += 1
        #                elif [i, j] in walls:
        #                    print("#", end="")
        #                elif [i, j] == robot:
        #                    print("@", end="")
        #                else:
        #                    print(".", end="")
        #                j += 1
        #            print()
        #        print("robot moving")
        #        print(robot, m)
        m_index = move_list.index(m)
        direction = directions[m_index]
        box_indexes = []
        to_check = [[robot[0], robot[1]]]
        box_right = [[x, y + 1] for x, y in boxes]
        while True:
            next_check = []
            for pos in to_check:
                pos = [pos[0] + direction[0], pos[1] + direction[1]]
                box_index = -1
                if pos in boxes:
                    box_index = boxes.index(pos)
                elif pos in box_right:
                    box_index = box_right.index(pos)
                if box_index != -1:
                    box_indexes.append(box_index)
                    if m_index == 0:
                        next_check.append([pos[0], pos[1] - 1])
                    elif m_index == 1:
                        next_check.append([pos[0], pos[1] + 1])
                    elif m_index == 2 or m_index == 3:
                        left = boxes[box_index]
                        right = box_right[box_index]
                        next_check.extend([[left[0], left[1]], [right[0], right[1]]])
                else:
                    if pos in walls:
                        box_indexes.append(-1)
                        break
            if len(next_check) == 0:
                break
            to_check = next_check
        if len(box_indexes) and -1 in box_indexes:
            continue
        robot = [robot[0] + direction[0], robot[1] + direction[1]]
        for index in set(box_indexes):
            boxes[index][0] += direction[0]
            boxes[index][1] += direction[1]
    gps = 0
    for box in boxes:
        print(box)
        gps += box[0] * 100 + box[1]
    print(gps)


def main():
    file = "inputs.txt"
    new_lines = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("#", "##")
            line = line.replace("O", "[]")
            line = line.replace(".", "..")
            line = line.replace("@", "@.")
            new_lines.append(line)
    robot = []
    boxes = []
    walls = []
    moves = []
    for i, line in enumerate(new_lines):
        for j, c in enumerate(line):
            print(c, end="")
            if c == "#":
                walls.append([i, j])
            elif c == "[":
                boxes.append([i, j])
            elif c == "@":
                robot.append([i, j])
            elif c in "<v>^":
                moves.append(c)
        print()
    input()
    print(robot, boxes, walls, moves)
    move_robot2(robot[0], boxes, walls, moves)


if __name__ == "__main__":
    main()
