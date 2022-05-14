'''
    Explanation:
        TC: O(n) where n is the number of transactions
        SC: O(n) to keep track of the frequencies of each item
'''

def solution1(transactions):
    dict = {}

    for i in transactions:
        dict[i] = dict.get(i, 0) + 1

    dict = sorted(dict.items(), key = lambda x:(-x[1], x[0]))
    # print("dict", dict)
    res = [' '.join([t[0], str(t[1])]) for t in dict]
    return res

print("solution1", solution1(['mouse', 'mouse', 'notebook', 'mouse', 'keyboard', 'printer', 'printer', 'printer']))


def solution2(transactions):
    inputDict = {}
    for i in transactions:
        if i in inputDict:
            inputDict[i] += 1
        else:
            inputDict[i] = 1
    
    freqCount = {}
    for i in inputDict:
        if inputDict[i] in freqCount:
            freqCount[inputDict[i]].append(i)
        else:
            freqCount[inputDict[i]] = [i]

    dict(sorted(freqCount.items()))

    res = []
    for i in freqCount:
        sortedFreqCount = sorted(freqCount[i])
        for j in sortedFreqCount:
            res.append(j + " " + str(i))
    return res

print("solution2", solution2(['mouse', 'mouse', 'notebook', 'mouse', 'keyboard', 'printer', 'printer', 'printer']))