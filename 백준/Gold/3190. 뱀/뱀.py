from collections import deque
# 동,남,서,북 (좌회전시 -1, 우회전시 +1)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input()) ## 배열 크기 N*N
K = int(input()) ## 사과의 개수

arr = [[0] * N for _ in range(N)] ## 일단 0으로 채운다. 사과 -1 뱀이 차지하는 영역 1

for _ in range(K):
    i, j = map(int, input().split()) ## 문제 똑바로 읽자... 1열 1행 == 최상단 1열 1행은 0,0
    arr[i-1][j-1] = -1 ## 사과 표시

L = int(input())
change = [] ## 방향 전환 정보를 넣을 list

for _ in range(L):
    second, dir = input().split()
    change.append((int(second), dir)) ## (몇초에, 어느방향)

sx, sy = 0, 0
arr[sx][sy] = 1 ## 출발점은 뱀이 차지하고 있음을..(1 == 뱀)
d, sec, idx = 0, 0, 0 #방향, 초 // idx는 change의 각 요소에 접근하기 위함이다.

q = deque()
q.append((sx,sy))

while True:
    sec += 1
    if sec-1 == change[idx][0]: # 초가 끝난 후에 방향 전환하므로 반복문의 맨 시작점에서 초-1로 체크하였다.
        if change[idx][1] == 'L':
            d = (d+3) % 4 ## 좌회전시 d의 인덱스가 -1씩
        elif change[idx][1] == 'D':
            d = (d+1) % 4 ## 우회전시 d의 인덱스가 +1씩
        if idx < L-1: ## change의 끝에서 두번째 요소까지만 idx+1이 이루어져야 에러 안 난다.
            idx += 1
    x, y = q[-1] ##x,y는 q의 가장 마지막
    nx, ny = x+dx[d], y+dy[d]
    if 0 <= nx < N and 0 <= ny < N:
        q.append((nx, ny))
        next = arr[nx][ny]
        if next == -1: ## 사과면
            arr[nx][ny] = 1 ## 몸이 늘어나고 이동하므로 꼬리 자를 필요 x
        elif next == 0: ## 사과가 없으면..
            arr[nx][ny] = 1
            (tailx, taily) = q.popleft() ## 꼬리는 q의 가장 첫 인덱스이다..
            arr[tailx][taily] = 0 ## 몸이 안 늘어나고 이동하므로..
        elif next == 1: ## 자기 몸과 만나면 종료
            break
    else:
        break

print(sec)

##최초 방향 오른쪽
