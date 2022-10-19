from collections import deque
# 동,남,서,북 (좌회전시 -1, 우회전시 +1)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = -1

L = int(input())
change = []

for _ in range(L):
    second, dir = input().split()
    change.append((int(second), dir))

sx, sy = 0, 0
arr[sx][sy] = 1
d, sec, idx = 0, 0, 0

q = deque()
q.append((sx,sy))
while True:
    sec += 1
    if sec-1 == change[idx][0]:
        if change[idx][1] == 'L':
            d = (d+3) % 4
        elif change[idx][1] == 'D':
            d = (d+1) % 4
        if idx < L-1:
            idx += 1
    x, y = q[-1]
    nx, ny = x+dx[d], y+dy[d]
    if 0 <= nx < N and 0 <= ny < N:
        q.append((nx, ny))
        next = arr[nx][ny]
        if next == -1:
            arr[nx][ny] = 1
        elif next == 0:
            arr[nx][ny] = 1
            (tailx, taily) = q.popleft()
            arr[tailx][taily] = 0
        elif next == 1:
            break
        x, y = nx, ny
    else:
        break

print(sec)

##최초 방향 오른쪽
