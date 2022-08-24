from collections import defaultdict
from collections import deque

def solution(start, end, rates):
    dict = defaultdict(list)
    
    for rate in rates:
        dict[rate[0]].append([rate[1], rate[2]])
        dict[rate[1]].append([rate[0], 1.0000/rate[2]])
        # Dict: {USD: [[JPY, 110], [AUD, 1.45]], (JPY: USD, 1/110), (USD: ), (AUD: USD, 1/1.45), (JPY: GBP, 0.007), (GBP: JPY, 1/0.007}
        # print(dict)
	
    q = deque([(start, 1.0000)])
    visited = set()
    visited.add(start)
    
    while q:
        curr, cost = q.popleft()
        # print(curr, cost)

        if curr == end: return round(cost, 2)
        # if curr in visited: continue
		
        for neighbors in dict[curr]:
            if neighbors[0] not in visited:
                q.append((neighbors[0], cost * neighbors[1]))
                visited.add(neighbors[0])

print(solution('GBP', 'AUD', [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]))