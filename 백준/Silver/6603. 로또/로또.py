def dfs(idx, n):
    if  n == 6:
        result.append(res[:])
        return
    for i in range(idx, k):
        res.append(S[i])
        dfs(i+1, n+1)
        res.pop()
while True:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break 
    k = arr[0]
    S = arr[1::]
    res = []
    result = []
    dfs(0, 0)
    for i in (result):
        print(*i)
    print()
## 걍 조합