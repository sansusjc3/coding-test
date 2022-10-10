def dfs(n):
    if  n == M:
        result.add(tuple(res))
        return
    for i in num:
        res.append(i)
        dfs(n+1)
        res.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
res = []
result = set()
dfs(0)
for i in sorted(list(result)):
    print(*i)
## 넣고 다시 뽑는 구조
## N과 M(10)은 넣지 않고 뽑는 구조