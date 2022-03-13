def solution(n):
    if n == 1:
        return 0

    elif n % 2 == 0:
        return 1 + solution(n // 2)
    
    else:
        return 1 + min(solution(n + 1), solution(n - 1))