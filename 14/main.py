def tick(p, v, steps, xb, yb, state):
    for i in range(steps):
        p[0] += v[0]
        p[1] += v[1]
        p[0] = (p[0] + xb) % xb
        p[1] = (p[1] + yb) % yb
    if (p[0], p[1]) in state:
        state[(p[0], p[1])] += 1
    else:
        state[(p[0], p[1])] = 1


def main():
    file = "inputs.txt"
    with open(file) as f:
        lines = f.readlines()
    print(len(lines))
    i = 1
    x_deviations = []
    y_deviations = []
    while True:
        state = {}
        for line in lines:
            p, v = line.split(" ")
            p = [int(n) for n in p[p.index("=") + 1 :].split(",")]
            v = [int(n) for n in v[v.index("=") + 1 :].split(",")]
            tick(p, v, i, 101, 103, state)
        pts = state.keys()
        x = [p[0] for p in pts]
        y = [p[1] for p in pts]
        x_avg = sum(x) / len(x)
        y_avg = sum(y) / len(y)
        x_dev = sum([(p[0] - x_avg) ** 2 for p in pts]) / len(x)
        x_deviations.append(x_dev)
        y_dev = sum([(p[1] - y_avg) ** 2 for p in pts]) / len(y)
        y_deviations.append(y_dev)
        if i >= 300:
            break
        i += 1
    print(min(x_deviations), x_deviations.index(min(x_deviations)))
    print(min(y_deviations), y_deviations.index(min(y_deviations)))
    n = max(
        x_deviations.index(min(x_deviations)), y_deviations.index(min(y_deviations))
    )
    t = min(
        x_deviations.index(min(x_deviations)), y_deviations.index(min(y_deviations))
    )
    if x_deviations.index(min(x_deviations)) == n:
        a = 101
        b = 103
    else:
        a = 103
        b = 101
    n += 1
    t += 1
    print(n, t, a, b)
    while n % b != t:
        n += a
    print(n)


if __name__ == "__main__":
    main()
