'''
    TC: O(n) 
'''

def solution(transactions):
    dict = {}

    for i in transactions:
        dict[i] = dict.get(i, 0) + 1

    dict = sorted(dict.items(), key = lambda x:(-x[1], x[0]))
    # print("dict", dict)
    res = [' '.join([t[0], str(t[1])]) for t in dict]
    return res

print(solution(['mouse', 'mouse', 'notebook', 'mouse', 'keyboard', 'printer', 'printer', 'printer']))