from copy import deepcopy
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(n):
    if n == 3: ## 3개가 되면
        BFS() ## 탐색한다.
        return
    for i in range(N):
        for j in range(M):
            if Arr[i][j] == 0:
                Arr[i][j] = 1  ## 좌표를 다 뽑아서
                dfs(n+1)
                Arr[i][j] = 0
def BFS():
    global maxV
    q = deque()
    arr = deepcopy(Arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2: ## 바이러스라면
                q.append((i, j)) ## q에 넣어주고
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny <M and arr[nx][ny] == 0: ## 바이러스가 퍼질 수 있다면
                arr[nx][ny] = 2 ## 확산하고
                q.append((nx, ny)) ## 확산된 자리에서 또 퍼질 수 있으므로, append 해준다.

    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: ## while문(바이러스 확산)이 다 끝났는데도 안전구역이라면
                res += 1 ## 카운트
    if maxV < res: ##최댓값 
        maxV = res
    return

N, M = map(int, input().split())
Arr = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
dfs(0)
print(maxV)

