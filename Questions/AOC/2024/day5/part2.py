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

def get_incorrectly_ordered_updates(updates, rules):
    res = []

    for update in updates:
        if not is_in_order(update, rules):
            res.append(update)
    return res

def reorder_update(update, rules):
    new_update_in_order = []
    
    for num in update:
        inserted = False
        for x, y in enumerate(new_update_in_order):
            if (num, y) in rules:
                new_update_in_order.insert(x, num)
                inserted = True
                break
        if not inserted:
            new_update_in_order.append(num)

    return new_update_in_order

# 75,97,47,61,53 becomes 97,75,47,61,53
# 61,13,29 becomes 61,29,13
# 97,13,75,29,47 becomes 97,75,47,29,13
# 97|75
# 75|47
# 47|61
# 61|53

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
    updates_not_in_order = get_incorrectly_ordered_updates(updates, rules)
    updates_in_order = [reorder_update(update, rules) for update in updates_not_in_order]
    medians = [get_median(update) for update in updates_in_order]
    res = 0

    for median in medians:
        res += median
    return res

print(solution("input.txt"))