from copy import deepcopy
from more_itertools import distinct_combinations


def main():
    with open("inputs.txt") as f:
        lines = [f.strip() for f in f.readlines()]
    split = lines.index("")

    def operate(a, b, op):
        if op == "AND":
            return a & b
        if op == "OR":
            return a | b
        if op == "XOR":
            return a ^ b

    values = dict()
    stack = {}
    for i, line in enumerate(lines):
        if i < split:
            key, value = line.split(": ")
            values[key] = int(value)
        if i > split:
            in1, op, in2, _, out = line.split(" ")
            stack[out] = (in1, in2, op)

    def build_bits(values, dependencies):
        stack = deepcopy(dependencies)
        while stack:
            for key in list(stack.keys()):
                in1, in2, op = stack[key]
                if in1 in values and in2 in values:
                    values[key] = operate(values[in1], values[in2], op)
                    stack.pop(key)

    build_bits(values, stack)
    binary = "".join(
        [
            str(values[key])
            for key in sorted(values.keys(), reverse=True)
            if key.startswith("z")
        ]
    )
    print(int(binary, 2))

    # for full adder
    # z_bit = (x_bit XOR y_bit) XOR carry_in
    # carry_out = (x_bit AND y_bit) OR ((x_bit XOR y_bit) AND carry_in)
    # for half adder
    # z_bit = x_bit XOR y_bit
    # carry_out = x_bit AND y_bit
    wrong = set()
    for out, (in1, in2, op) in stack.items():
        # z_bits always result from XOR except last bit which is the carry
        if out[0] == "z" and op != "XOR" and int(out[1:]) != len(binary) - 1:
            wrong.add(out)
        elif op == "XOR":
            for _in1, _in2, _op in stack.values():
                # XOR results used in XOR and AND
                if out in [_in1, _in2] and _op == "OR":
                    wrong.add(out)
                # XOR must be connected to at least x,y or z
                if all(v[0] not in "xyz" for v in [in1, in2, out]):
                    wrong.add(out)
        elif op == "AND" and set(["x00", "y00"]) != set([in1, in2]):
            # AND results that is not x00 and y00 only used in OR
            for _in1, _in2, _op in stack.values():
                if out in [_in1, _in2] and _op != "OR":
                    wrong.add(out)
    print(",".join(sorted(list(wrong))))


if __name__ == "__main__":
    main()
