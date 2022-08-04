from itertools import product


def getProduct(left, right, arr):
    prodResult = 1
    for i in range(left, right + 1):
        prodResult *= arr[i]
    return prodResult

def getQueryResults(n, queries):
    data, output, res = [], [], []

    while n:
        data.append(n % 2)
        n //= 2

    for i in range(len(data)):
        if data[i] == 1:
            output.append(2 ** i)
    
    for query in queries:
        left = query[0] - 1
        right = query[1] - 1
        middle = query[2]

        product = getProduct(left, right, output)

        res.append(product % middle)
    
    return res