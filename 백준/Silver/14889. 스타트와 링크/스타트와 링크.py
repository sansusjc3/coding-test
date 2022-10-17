def dfs(idx, n):
    global minV
    if n == N//2:
        S, L = 0, 0
        for i in range(N-1):  ##[(0,1) (0,2) ... (1,2) (1,3)... (3,4) ... ) [0]이 무조건 [1]보다 작게 하여 조금 덜 탐색
            for j in range(i+1, N):
                if start[i] and start[j]: ## 1표시라면,,, == start팀이라면
                    S += arr[i][j]
                    S += arr[j][i]## S에 더해주고
                elif not start[i] and not start[j]:
                    L += arr[i][j]
                    L += arr[j][i]##아니면 L에 더해준다.
        res = abs(S-L)
        if minV > res:
            minV = res
            if minV == 0:
                return
        return

    for i in range(idx, N):
        if not start[i]:
            start[i] = 1
            dfs(i+1, n+1)
            start[i] = 0
##부분집합처럼 접근하였다.

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = [0 for _ in range(N)]
minV = 1000000
dfs(0, 0)
print(minV)