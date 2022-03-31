import heapq

def minimumTime(n, ability, processes):

    max_heap = []
    for ab in ability:
        heapq.heappush(max_heap, -ab)

    time = 0

    while processes > 0:
        max_ab = -heapq.heappop(max_heap)

        processes -= max_ab

        max_ab //= 2

        heapq.heappush(max_heap, -max_ab)

        time += 1

    return time