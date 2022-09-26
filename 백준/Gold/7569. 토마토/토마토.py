from collections import deque
dx = [0, 1, 0, -1, 0, 0] ## 우 밑 좌 상(시계방향)
dy = [1, 0, -1, 0, 0, 0] ## 위 아래
dz = [0, 0, 0, 0, 1, -1] ## 가장 밑에 상자부터 들어오므로

def BFS():
    while queue:
        global day
        z, x, y, day = queue.popleft()  ## 튜플에 저장해 놓은 day를 통해 global day를 계속 갱신해준다.
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]            
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and arr[nz][nx][ny] == 0: ## 익힐 수 있는 과일이 있다면
                arr[nz][nx][ny] = 1 ## 익히고
                queue.append((nz, nx, ny, day+1)) ## day+1일차 현황판에 반영해준다. 이후 0일차 튜플이 다 pop되고나면 >>> 1일차에 새로 익은 과일을 기준으로 처리 출발.
                                                  ## (queue가 비어있다 == 더 이상 처리할 게 없다는 것)은 n일차에 더 이상 익힐 과일이 없다는 뜻이다. == 작업종료
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
day = 0
queue = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 1:
                queue.append((z,x,y,0)) ## 0일차에 익어있던 과일로 처리 출발
BFS()

for h in range(H):
    for x in range(N):
        for y in range(M):
            if arr[h][x][y] == 0:
                day = -1 ## 작업이 끝났는데 안 익은 과일이 있다면 -1 출력

print(day)