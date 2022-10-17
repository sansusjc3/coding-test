dx = [-1, 0, 1, 0]  ## 북, 동, 남, 서
dy = [0, 1, 0, -1]   # (문제 제시, 봐야 할 방향) ex(북, 서) (동, 북)

def clean():
    global res
    global d
    x, y = sx, sy
    while True:
        for _ in range(4):
            d = (d+3)%4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                if visited[nx][ny] == 0:##청소할 곳이라면
                    visited[nx][ny] = 1  ## 청소하고
                    x, y = nx, ny  ## 전진
                    res += 1  ## 했어용~
                    break  ## 다음 좌표에서 탐색해야 하니까 break
        else:  ## 네 방향 다 봤는데 청소 못했으면..
            if arr[x - dx[d]][y - dy[d]] != 1:  ## 후진 가능하면
                x, y = x - dx[d], y - dy[d] # 후진하고
            else:  ## 못하면
                return

N, M = map(int, input().split())
sx, sy, d = map(int, input().split())  # d==0북, d==1동, d==2남, d==3서
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
res = 0
if arr[sx][sy] == 0:
    res += 1
visited[sx][sy] = 1
clean()
print(res)