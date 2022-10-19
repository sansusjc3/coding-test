def dfs(idx, n):
    if  n == 6:
        result.append(res[:])
        return
    for i in range(idx, k):
        res.append(S[i])
        dfs(i+1, n+1)
        res.pop()
while True:
    arr = list(map(int, input().split())) ##while안에서 번호를 받다가
    if arr == [0]: ## 0이 들어오면 종료이므로...
        break 
    k = arr[0] # 첫 인덱스가 개수이므로
    S = arr[1::]
    res = [] ##조합을 완성시킬 리스트
    result = [] ## 완성된 조합을 넣을 리스트
    dfs(0, 0)
    for i in (result):
        print(*i)
    print()
## 걍 조합
