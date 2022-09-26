from collections import deque
dx = [1, 2, 2, 1, -1, -2, -2, -1] ## 체스 이동 가능 방향
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def BFS(x, y, cnt):
    queue = deque()
    queue.append((x,y,cnt))
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if x == ex and y == ey: ## 도착점이 꺼내졌다면
                return print(cnt) ## 몇번만에 왔는지 출력한다.
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1              

for tc in range(int(input())):
    N = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1 ## 출발점으로 왔다갔다 안하기 위함.
    BFS(sx, sy, 0)