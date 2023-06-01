from collections import deque
def dfs(idx, n, S, Y):
    global res
    if Y >= 4: ## 다솜파 될 수 없음
        return

    if n == 7: ## 7명이 됐을 때
        if S >= 4 and is_Adj(com): ## 다솜파 조건을 만족하고 인접해 있다면
            res += 1 ## 다솜파 카운팅
        return
    else:
        for i in range(idx, 25):
            com.append(loc[i])
            if loc[i][2] == 'S':
                dfs(i+1, n+1, S+1, Y)
            else:
                dfs(i+1, n+1, S, Y+1)
            com.pop()

def is_Adj(lst): ##인접성 체크를 위한 BFS
    visited = [[0 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append(lst[0])
    visited[lst[0][0]][lst[0][1]] = True
    result = 0
    while q:
        x, y, who = q.popleft()
        result += 1
        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx = x+ dx
            ny = y + dy
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[nx][ny]: 
                if (nx, ny, arr[nx][ny]) in lst: ##조건을 만족하는 새 좌표가 com안에 있으면
                    q.append((nx, ny, arr[nx][ny])) ##(com안의 좌표를 기준으로 인접 확인이기 떄문에)
                    visited[nx][ny] = 1

    if result == len(lst): ##7개가 인접해 있다면..
        return True
    else:
        return False            

arr = [list(input()) for _ in range(5)]
loc = [] ## 전체 (위치, who)를 넣을 lst
com = []
res = 0
for i in range(5):
    for j in range(5):
        loc.append((i, j, arr[i][j])) ##(x, y, who)
dfs(0, 0, 0, 0) ## (조합을 위한, 조합을 위한, S카운트, Y카운트)
print(res)