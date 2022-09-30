from collections import Counter

def boxes(weights):
    counts = Counter(weights)
    ans = 0
    for k, v in counts.items():
        if v %2 ==1 and v % 3==1:
            return -1
        else:
            ans += v//3
            ans += 1 if v % 3!=0 else 0
    return ans