def plusMult(A):
    rEven = rOdd = 0

    for i in range(0, len(A), 4):
        rEven += A[i]
        if (i + 2) < len(A): rEven += A[i + 2]
    
    for i in range(1, len(A), 4):
        rOdd += A[i]
        if (i + 2) < len(A): rOdd += A[i + 2]

    if rEven < 0: rEven *= -1
    if rOdd < 0: rOdd *= -1

    rEven %= 2
    rOdd %= 2

    if rOdd > rEven: return "ODD"
    elif rOdd < rEven: return "EVEN"
    else: return "NEUTRAL"