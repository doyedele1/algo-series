# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq

def solution(A, B, C):
    # write your code in Python 3.6
    chars = "abc"
    maxHeap = []

    if A: heapq.heappush(maxHeap, (-A, 0))
    if B: heapq.heappush(maxHeap, (-B, 1))
    if C: heapq.heappush(maxHeap, (-C, 2))

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