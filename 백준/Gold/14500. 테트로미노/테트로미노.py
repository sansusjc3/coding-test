dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(n, x, y, Sum):
    global maxV
    if n == 1:
        if maxV > Sum + best * 3:
            return
    if n == 4:
        if Sum > maxV:
            maxV = Sum
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(n + 1, nx, ny, Sum + arr[nx][ny])
            visited[nx][ny] = 0


def fuck(n, x, y, Sum):
    global maxV
    if n == 1:
        if maxV > Sum + best * 3:
            return
    if n == 4:
        if Sum > maxV:
            maxV = Sum
        return
    if n >= 2:
        x, y = sx, sy
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            fuck(n + 1, nx, ny, Sum + arr[nx][ny])
            visited[nx][ny] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maxV = 0
best = 0
for lst in arr:
    best = max(max(lst), best)

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, i, j, arr[i][j])
        sx, sy = i, j
        fuck(1, i, j, arr[i][j])
        visited[i][j] = 0
print(maxV)