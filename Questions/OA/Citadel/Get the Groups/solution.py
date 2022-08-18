def maxCircle(queries):
    def find(e):
        if not parents[e]:
            parents[e] = e
            size[e] = 1
            return e

        if e == parents[e]: return e
        
        rep = find(parents[e])
        parents[e] = rep
        return rep

    def union(i, j):
        pi = find(i)
        pj = find(j)

        size[pi] += size[pj]
        parents[pj] = pi
    
    res = []
    _max = 0
    parents, size = {}, {}
        
    for i in range(len(queries)):
        p1 = find(queries[i][0])
        p2 = find(queries[i][1])

        if p1 != p2:
            union(p1, p2)
            if size[p1] > _max:
                _max = size[p1]
        res[i] = _max
    
    return res