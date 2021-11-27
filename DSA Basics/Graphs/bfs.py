# TC - O(V+E)
# SC - O(V)

def bfs(Node start):
    queue = LinkedList(start)
    seen = set()

    queue.add(start)

    while queue:
        curr = queue.pop()

        if not curr in seen:
            seen.add(curr)
            print(curr)
        
        for adjacent in adjacents(curr):
            if not adjacent in seen:
                queue.add(adjacent)