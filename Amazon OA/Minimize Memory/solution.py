def solution(processes, m):
    window_start = 0
    total_sum = sum(processes)
    pref_sum = 0
    max_sum = 0

    for i in range(len(processes)):
        win_size = (i-window_start)+1
        pref_sum+= processes[i]
        if win_size==m:
            max_sum= max(max_sum, pref_sum)
            pref_sum-=processes[window_start]
            window_start+=1

    output = total_sum- max_sum
    return output