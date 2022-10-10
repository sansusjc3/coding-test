def dfs(idx, n):
    if n == M:
        result.add(tuple(res))
        return
    for i in range(idx, N):
        res.append(num[i])
        dfs(i+1, n+1)
        res.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
res = []
result = set()
dfs(0, 0)

for i in sorted(list(result)):
    print(*i)