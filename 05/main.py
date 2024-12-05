from collections import defaultdict, deque


def build_page_order(page_order_rules):
    graph = defaultdict(list)
    for rule in page_order_rules:
        before, after = rule.split("|")
        before, after = before.strip(), after.strip()
        graph[before].append(after)
    return graph


def validate_update(page_update, page_order):
    for i, page in enumerate(page_update):
        if page in page_order.keys():
            if any([page_update[j] in page_order[page] for j in range(i)]):
                return False
    return True


def correct_update(page_update, page_order):
    indegree = defaultdict(int)
    dependencies = [page_order[page] for page in page_update]
    for page in page_update:
        indegree.setdefault(page, 0)
        for value in dependencies:
            if page in value:
                indegree[page] += 1
    queue = deque(page for page in page_update if indegree[page] == 0)
    new_update = []
    while queue:
        page = queue.popleft()
        new_update.append(page)
        for value in page_order[page]:
            indegree[value] -= 1
            if indegree[value] == 0:
                queue.append(value)
    return new_update


def main():
    file = "inputs.txt"
    page_order_rules = []
    page_updates = []
    with open(file, "r") as f:
        lines = f.readlines()
        switch = False
        for line in lines:
            if line == "\n":
                switch = True
                continue
            (
                page_order_rules.append(line.strip())
                if not switch
                else page_updates.append(line.strip().split(","))
            )
    page_order = build_page_order(page_order_rules)
    valid_updates = []
    invalid_updates = []
    for page_update in page_updates:
        if validate_update(page_update, page_order):
            valid_updates.append(page_update)
        else:
            invalid_updates.append(page_update)
    correct_count = 0
    for update in valid_updates:
        correct_count += int(update[len(update) // 2])
    print(f"Correct Count: {correct_count}")
    new_updates = []
    for invalid_update in invalid_updates:
        new_updates.append(correct_update(invalid_update, page_order))
    new_count = 0
    for update in new_updates:
        new_count += int(update[len(update) // 2])
    print(f"New Count: {new_count}")


if __name__ == "__main__":
    main()
