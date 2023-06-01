import sys

N = int(sys.stdin.readline())
tower = [0] + list(map(int, sys.stdin.readline().split()))
stack = []
res = [0] * (N + 1)

for idx in range(1, N + 1):
    height = tower[idx]
    while stack:
        if tower[stack[-1]] > height:
            res[idx] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(idx)

print(*res[1:])
