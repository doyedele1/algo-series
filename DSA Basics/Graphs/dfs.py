# TC - O(V+E)
# SC - O(V)

def dfs(Node start):
    stack = [node]
    seen = set()

    stack.push(start)
    
    while stack:
        curr = stack.pop() # pull a node

        if not curr in seen:
            seen.add(curr) # process if not seen
            print(curr) # process if not seen

        for adjacent in adjacents(curr):
            if not adjacent in seen:
                stack.push(adjacent) # add unseen children