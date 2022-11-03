def findMinHealth(power, armor):
    n = len(power)
    res = 0
    arm = True
    for i in range(n):
        if power[i] > armor and arm == True:
            res += power[i] - armor
            arm = False
        else:
            res += power[i]
    if arm == True:
        temp = max(power)
        res -= temp
        arm = False
    return res + 1