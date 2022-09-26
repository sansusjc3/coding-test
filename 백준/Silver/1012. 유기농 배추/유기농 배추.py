from collections import deque
dx = [0, 1, 0, -1] ## 우 밑 좌 상(시계방향)
dy = [1, 0, -1, 0] 

def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0

    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx,ny))

for tc in range(int(input())):
    M, N, K = map(int, input().split()) 
    arr = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().split()) ## x,y 입력이 좌표식으로 들어옴(주의)
        arr[x][y] = 1

    for i in range(N): ## 각 좌표별로
        for j in range(M):
            if arr[i][j] == 1: ## 배추일 경우
                BFS(i, j) ## 벌레 이동 시켜주고
                cnt += 1 ## 벌레가 더 이상 갈 배추 없으면 cnt 올려준다.
    print(cnt)
