def process_input(inp):
    rules_section, updates_section = inp.strip().split("\n\n")
    rules, updates = [], []
    
    for line in rules_section.splitlines():
        rules.append(tuple(map(int, line.split("|"))))
    for line in updates_section.splitlines():
        updates.append(tuple(map(int, line.split(","))))

    return rules, updates

def is_in_order(update, rules):
    update_map = {}
    for i, num in enumerate(update):
        update_map[num] = i
    
    for x, y in rules:
        if x in update_map and y in update_map:
            if update_map[x] > update_map[y]:
                return False
    return update

def get_updates_in_order(updates, rules):
    res = []

    for update in updates:
        if is_in_order(update, rules):
            res.append(update)
    return res

def get_median(update):
    n = len(update)
    mid = n // 2

    if n % 2 == 1:
        return update[mid]
    else:
        return (update[mid - 1] + update[mid]) // 2

def solution(file_path):
    with open(file_path, 'r') as f:
        inp = f.read()

    rules, updates = process_input(inp)
    updates_in_order = get_updates_in_order(updates, rules)
    medians = [get_median(update) for update in updates_in_order]
    res = 0

    for median in medians:
        res += median
    return res

print(solution("input.txt"))