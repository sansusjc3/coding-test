from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def BFS():
    q = deque()
    arr[sx][sy] = 0
    q.append((sx, sy))
    cnt_1 = 0
    while q:
        x, y = q.popleft()
        cnt_1 += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0
    return cnt_1

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            sx, sy = i, j
            lst.append(BFS())
            cnt += 1
lst.sort()
print(cnt)
for l in lst:
    print(l)