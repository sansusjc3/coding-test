import sys
import heapq

N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
q = []
res = 0

for _ in range(N):
    dead, cup = map(int, sys.stdin.readline().split())
    arr[dead].append(cup)

for idx in range(N, 0, -1):
    for cup in arr[idx]:
        heapq.heappush(q, -cup)
    if q:
        res -= heapq.heappop(q)
print(res)