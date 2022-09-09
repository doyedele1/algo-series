from collections import defaultdict, deque

def get_second_degree_friends(graph, user):
    new_graph = defaultdict(list)

    for key in graph:
        new_graph[key] = graph[key]

    output = []
    done = False
    q = deque([(user, 0)])

    while q:
        if done: break

        for user in range(len(q)):
            curr_user, curr_level = q.popleft()
            # print(curr_user, curr_level)

        if curr_level == 2:
            output.append(curr_user)
            done = True
            # print(output)

        children = new_graph[curr_user]
        for child in children:
            q.append((child, curr_level + 1))
            # print(q)

    return output

print(get_second_degree_friends({
    "A": ["B","C"],
    "B": ["D","E","F"],
    "C": ["G"],
    "D": ["H"]
}, "A"))