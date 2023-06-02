import sys
import heapq

N = int(sys.stdin.readline())
minQ, maxQ = [], []

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(minQ) == len(maxQ):
        heapq.heappush(minQ, -num)
    else:
        heapq.heappush(maxQ, num)

    if minQ and maxQ and -minQ[0] > maxQ[0]:
        heapq.heappush(minQ, -heapq.heappop(maxQ))
        heapq.heappush(maxQ, -heapq.heappop(minQ))
    print(-minQ[0])