from collections import defaultdict
from collections import deque

def solution(start, end, rates):
    graph = defaultdict(list)
    
    for rate in rates:
        graph[rate[0]].append([rate[1], rate[2]])
        graph[rate[1]].append([rate[0], 1.0000/rate[2]])
        '''
            print(graph) returns
                graph: {
                    USD: [[JPY, 110], [AUD, 1.45]], 
                    JPY: [[USD, 1/110], [GBP, 0.007]], 
                    AUD: [[USD, 1/1.45]],
                    GBP: [[JPY, 1/0.007]]
                }
        '''
	
    q = deque([(start, 1.0000)])
    visited = set()
    visited.add(start)
    
    while q:
        curr, cost = q.popleft()
        # print(curr, cost)

        if curr == end: return round(cost, 2)
        # if curr in visited: continue
		
        for neighbors in graph[curr]:
            if neighbors[0] not in visited:
                q.append((neighbors[0], cost * neighbors[1]))
                visited.add(neighbors[0])

print(solution('GBP', 'AUD', [['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]]))