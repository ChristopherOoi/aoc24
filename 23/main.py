from collections import defaultdict


def main():
    graph = defaultdict(list)
    with open("inputs.txt") as f:
        for l in f:
            pairs = l.strip().split("-")
            graph[pairs[0]].append(pairs[1])
            graph[pairs[1]].append(pairs[0])
    seen = set()
    for k, v_list in graph.items():
        for v in v_list:
            con = {k, v}
            c3 = {k, v}
            for _v in graph[v]:
                if all(_v in graph[co] for co in con):
                    con.add(_v)
                if all(_v in graph[c] for c in c3):
                    c3.add(_v)
                if len(c3) == 3:
                    seen.add(tuple(sorted(c3)))
                    c3 = {k, v}
            seen.add(tuple(sorted(con)))
    seen = [s for s in seen if any(_s[0] == "t" for _s in s)]
    print(sum([len(s) == 3 for s in seen]))
    seen = sorted(seen, key=lambda x: len(x), reverse=True)
    print(",".join(sorted(seen[0])))


if __name__ == "__main__":
    main()
