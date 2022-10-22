def dfs(idx, n):
    global minV
    if n == M:
        res = check_distance()
        minV = min(minV, res)
        return
    for i in range(idx, len(tmp)):
        comb.append(tmp[i])
        dfs(i+1, n+1)
        comb.pop()

def check_distance():
    dis = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                d = 100
                for k in range(M):
                    d = min((abs(comb[k][0] - i) + abs(comb[k][1] - j)), d)
                dis += d
    return dis

N, M = map(int, input().split()) ## N(가로,세로) M(폐업 안 할)
arr = [list(map(int, input().split())) for _ in range(N)]
#r,c는 1부터
minV = 100000
tmp = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            comb = []
            tmp.append((i, j))

dfs(0,0)
print(minV)