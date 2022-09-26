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
            if x == ex and y == ey:
                return print(cnt)
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1              

for tc in range(int(input())):
    N = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    BFS(sx, sy, 0)