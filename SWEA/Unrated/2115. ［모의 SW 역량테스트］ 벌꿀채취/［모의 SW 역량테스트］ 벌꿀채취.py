def dfs(cnt, honey, honeyV):
    global maxV
    if honey > C:
        return

    if cnt == M:
        maxV = max(maxV, honeyV)
        return

    dfs(cnt+1, honey, honeyV)
    dfs(cnt+1, honey+bowl[cnt], honeyV+bowl[cnt]**2)

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * (N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            maxV = 0
            bowl = arr[i][j:j+M]
            dfs(0, 0, 0)
            result[i][j] = maxV

    res = 0
    if M*2 <= N:
        for i in range(N):
            for j in range(N-2*M+1):
                for k in range(j+M, N-M+1):
                    res = max(res, result[i][j] + result[i][k])
    row = []
    for r in result:
        row.append(max(r))
    row.sort()
    res = max(res, row[-1] + row[-2])

    print(f'#{tc} {res}')