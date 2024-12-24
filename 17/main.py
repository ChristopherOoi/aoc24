def get_operand(operand, regA, regB, regC):
    if operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC
    else:
        return operand


def process(regA, regB, regC, program):
    out = []
    i = 0
    operations = []
    while True:
        try:
            opc = program[i]
            ope = program[i + 1]
            if ope == 7:
                print("ERROR!")
                break
            if opc == 0:
                num = regA
                div = 2 ** get_operand(ope, regA, regB, regC)
                regA = num // div
            elif opc == 1:
                regB = regB ^ ope
            elif opc == 2:
                regB = get_operand(ope, regA, regB, regC) % 8
            elif opc == 3:
                if regA != 0:
                    i = get_operand(ope, regA, regB, regC)
                    continue
            elif opc == 4:
                regB = regB ^ regC
            elif opc == 5:
                out.append(get_operand(ope, regA, regB, regC) % 8)
            elif opc == 6:
                num = regA
                div = 2 ** get_operand(ope, regA, regB, regC)
                regB = num // div
            elif opc == 7:
                num = regA
                div = 2 ** get_operand(ope, regA, regB, regC)
                regC = num // div
            state = [i, regA, regB, regC, opc, ope]
            operations.append(state)
            i += 2
        except:
            break
    out = ",".join([str(o) for o in out])
    return operations, out


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = f.readlines()
        lines = [
            l.strip() for l in [line.split(":")[1] for line in lines if ":" in line]
        ]
    print(lines)
    regA = int(lines[0])
    regB = int(lines[1])
    regC = int(lines[2])
    program = [int(n) for n in lines[3].split(",")]
    oct_str = "0o"
    run = True
    while run:
        for i in range(8):
            temp = oct_str + str(i)
            print(temp)
            _, out = process(int(temp, 8), regB, regC, program)
            if ",".join([str(o) for o in program]).endswith(out):
                oct_str = temp
                if ",".join([str(o) for o in program]) == out:
                    run = False
                break
        else:
            if oct_str.endswith("7"):
                i = len(oct_str) - 1
                while oct_str[i] == "7":
                    i -= 1
                oct_str = oct_str[: i + 1]
            digit = int(oct_str[-1])
            digit += 1
            oct_str = oct_str[:-1] + str(digit)
    print(oct_str, int(oct_str, 8))
    print(out, program)
    operations = process(regA, regB, regC, program)


if __name__ == "__main__":
    main()
