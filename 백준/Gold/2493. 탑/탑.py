from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
tower = [0] + list(map(int, input().split()))
stack = deque()
res = deque()

for i in range(1, N+1):
    while stack:
        if stack[-1][1] > tower[i]:
            res.append(stack[-1][0])
            break
        else:
            stack.pop()
    else:
        res.append(0)
    stack.append([i, tower[i]])
print(*res)