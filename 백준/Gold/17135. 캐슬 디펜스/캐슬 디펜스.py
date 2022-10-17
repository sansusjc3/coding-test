from copy import deepcopy

def dfs(idx, n):
    global arr
    if n == 3: ## 궁수 3명이 모이면
        comb.sort()
        arr = deepcopy(ARR) ##input 카피한 arr가지고
        hunt(comb, 0, 0, 0) #헌트시작
        return

    for i in range(idx, M): ## 조합 코드
        comb.append(tmp[i])
        dfs(i + 1, n + 1)
        comb.pop()


def hunt(lst, n, res, cnt):
    global goal
    global maxV
    if goal == res: ## 모든 적을 잡았다면
        if maxV < res:
            maxV = res
            return
        return

    if cnt == N+1: ## 판이 다 내려와서 디펜스 게임이 끝났다면..
        if maxV < res:
            maxV = res
            return
        return

    if n == 3: ## 궁수 3명이 다 쐈으면..
        turn() ## 턴함수 호출(판을 내려주는)
        if cnt == N:
            if maxV < res:
                maxV = res
                return
        hunt(lst, 0, res, cnt+1)
        return

    dis = []

    for i in range(N - 1, N - 2 - D, -1): ## 궁수 사정거리 안에서의 세로좌표
        for j in range(M): ## 직선이 안 닿으면 대각도 안 닿기 때문에..
            if i >= 0:
                if arr[i][j] != 0:
                    d = abs(lst[n][0] - i) + abs(lst[n][1] - j)
                    if d <= D:
                        dis.append((d, j, i)) ## 거리, 가로, 세로 순으로..
            else:
                break

    if len(dis) > 0: 
        dis.sort() ## 문제에서 제시한 조건을 맞추기 위해 거리, 가로, 세로를 키로하여 정렬한다.
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
goal = 0  ## 잡을 수 있는 모든 적의 수
for i in range(N):
    for j in range(M):
        if ARR[i][j] == 1:
            goal += 1 ## 올려준다.
maxV = 0
for i in range(M):
    tmp.append((N, i)) ## 궁수 위치 tmp에 append하고 comb할 예정
dfs(0, 0)
print(maxV)