import sys
import heapq

N = int(sys.stdin.readline())
q = []

for _ in range(N):
    nums = map(int, sys.stdin.readline().split())
    for num in nums:
        if len(q) < N:
            heapq.heappush(q, num)
        else:
            if q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q, num)
print(q[0])