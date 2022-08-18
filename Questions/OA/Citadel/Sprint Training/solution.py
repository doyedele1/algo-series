def solution(n, sprints):
    incremental = [0] * (n + 2)
    
    for i in range(len(sprints) - 1):
        start = min(sprints[i], sprints[i + 1])
        end = max(sprints[i], sprints[i + 1])
        incremental[start] += 1
        incremental[end + 1] -= 1

    scores = [0] * (n + 1)
    score = 0

    for i in range(1, n + 1):
        score += incremental[i];
        scores[i] = score;

    res = dict()
    for i in range(1, n + 1):
        if scores[i] > res.get(0):
            res[i] = scores[i]
    return res.get()

print(solution(5, [2, 4, 1, 3]))