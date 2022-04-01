# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq

def solution(a, b, c):
    # write your code in Python 3.6
    chars = "abc"
    maxHeap = []

    if a: heapq.heappush(maxHeap, (-a, 0))
    if b: heapq.heappush(maxHeap, (-b, 1))
    if c: heapq.heappush(maxHeap, (-c, 2))

    previous, i = heapq.heappop(maxHeap)
    diverse = chars[i] * (1 + (previous != -1))
    previous += 2

    while maxHeap:
        current, j = heapq.heappop(maxHeap)
        if previous < 0:
            heapq.heappush(maxHeap, (previous, i))
        d = 1 + (current < (previous // 2) and current != -1)
        diverse += chars[j] * d
        previous, i = current + d, j

    return diverse