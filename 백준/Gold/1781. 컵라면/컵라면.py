import sys
import heapq

N = int(sys.stdin.readline())
arr = []
res = 0
for _ in range(N):
    dead, cup = map(int, sys.stdin.readline().split())
    arr.append((dead, cup))
arr.sort()
q = []
for problem in arr:
    heapq.heappush(q, problem[1])
    if problem[0] < len(q):
        heapq.heappop(q)
print(sum(q))