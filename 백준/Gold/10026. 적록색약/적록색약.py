from collections import deque

dx = [0, 1, 0, -1] ## 우 밑 좌 상(시계방향)
dy = [1, 0, -1, 0] 

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[x][y] == arr[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1


N = int(input())
arr = [list(input()) for _ in range(N)]
check = 0 ## 0일 때 색약 아닌 경우, 1일 때 색약인 경우
while True:
    cnt = 0 ## 색약으로 반복문 돌 때는 cnt 다시 뽑아야 하니까 초기화
    visited = [[0] * N for _ in range(N)] ## cnt와 마찬가지
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j)
                cnt += 1    ##bfs 실행횟수 만큼이 구역이다.
    print(cnt, end = ' ')
    if check == 1: 
        break ## 이미 색약인 경우를 처리 하였으므로 밑의 변경을 수행할 필요 없다.
    for i in range(N): 
        for j in range(N):
            if arr[i][j] == 'R': ## for문이 하나 끝나면 반복문 처리 1회가 끝난 것이므로
                arr[i][j] = 'G'  ## 색약을 위한 arr로 바꿔주고
    check += 1 ## 색약처리를 하러 넘어간다.                   
