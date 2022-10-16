from copy import deepcopy

def dfs(idx, n):
    global arr
    if n == 3:
        comb.sort()
        arr = deepcopy(ARR)
        hunt(comb, 0, 0, 0)
        return

    for i in range(idx, M):
        comb.append(tmp[i])
        dfs(i + 1, n + 1)
        comb.pop()


def hunt(lst, n, res, cnt):
    global goal
    global maxV
    if goal == res:
        if maxV < res:
            maxV = res
            return
        return

    if cnt == N+1:
        if maxV < res:
            maxV = res
            return
        return

    if n == 3:
        turn()
        if cnt == N:
            if maxV < res:
                maxV = res
                return
        hunt(lst, 0, res, cnt+1)
        return

    dis = []

    for i in range(N - 1, N - 2 - D, -1):
        for j in range(M):
            if i >= 0:
                if arr[i][j] != 0:
                    d = abs(lst[n][0] - i) + abs(lst[n][1] - j)
                    if d <= D:
                        dis.append((d, j, i))
            else:
                break

    if len(dis) > 0:
        dis.sort()
        for k in range(len(dis)):
            ti, tj = dis[k][2], dis[k][1]
            if arr[ti][tj] != 0:
                if arr[ti][tj] == 1:
                    res += 1
                    arr[ti][tj] = -1
                    break
                break
    hunt(lst, n + 1, res, cnt)


def turn():
    for i in range(N - 1, 0, -1):
        for j in range(M):
            arr[i][j] = arr[i - 1][j]
    for i in range(M):
        arr[0][i] = 0
    for i in range(N - 1, N - 2 - D, -1):
        for j in range(M):
            if i >=0 and arr[i][j] == -1:
                arr[i][j] = 0
    return

N, M, D = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]
arr = []
tmp = []
comb = []
goal = 0
for i in range(N):
    for j in range(M):
        if ARR[i][j] == 1:
            goal += 1
maxV = 0
for i in range(M):
    tmp.append((N, i))
dfs(0, 0)
print(maxV)