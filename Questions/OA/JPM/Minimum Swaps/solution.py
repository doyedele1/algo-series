def solution(arr):
    n = len(arr)
    arr_pos = [(arr[i], i) for i in range(n)]
    
    arr_pos.sort(reverse=True, key=lambda it: it[0])
    
    visited = [False] * n
    
    swaps = 0
    
    for i in range(n):
        if visited[i] or arr_pos[i][1] == i:
            continue
        
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][1]
            cycle_size += 1
        
        if cycle_size > 1:
            swaps += cycle_size - 1
    
    return swaps

arr = [3, 1, 2]
print(solution(arr))