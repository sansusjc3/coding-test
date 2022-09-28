from collections import deque

dx = [0, 1, 0, -1] ## 우 밑 좌 상(시계방향)
dy = [1, 0, -1, 0] 

def escape():
    while sq: ## 더 이상 탈출시도를 할 수 없을 때까지 (불, 상근 탈출) 방식으로 이어 나간다. 불이 붙으려는 칸도 갈 수 없기 때문에 순서에 주의
        for _ in range(len(fq)): 
            fx, fy = fq.popleft()
            for i in range(4):
                nx = fx + dx[i]
                ny = fy + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == '.': ## 불 퍼질 수 있으면
                        arr[nx][ny] = '*'  ## 불 지르고
                        fq.append((nx, ny)) ## fq에 퍼진 불 넣어준다.
        for _ in range(len(sq)): 
            sx, sy = sq.popleft()
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[sx][sy] + 1
                        sq.append((nx, ny))
                else: ## 현재 위치에서 탐색했는데 배열 밖으로 나갈 수 있다면..
                    return visited[sx][sy] ## 몇번만에 탈출인지 return해준다. 시작부터 1을 넣었기 때문에 별도의 처리 X                    
    return 'IMPOSSIBLE' ## sq가 빌 때까지 탈출을 못했다면...

T = int(input())
for tc in range(1, T+1):
    W, H = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    fq = deque() ## 불
    sq = deque() ## 상근이
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '*': ## 불인 경우
                fq.append((i, j))
            elif arr[i][j] == '@': ## 상근이
                x, y = i, j
                sq.append((i, j))
    visited = [[0] * W for _ in range(H)]
    visited[x][y] = 1 ## 출발점

    print(escape())