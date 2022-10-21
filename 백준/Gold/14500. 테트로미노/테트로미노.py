dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(n, x, y, Sum):
    global maxV
    
    if n <= 3:
        if maxV > Sum + best * (4-n): # 남은 기회 * 최선의 숫자를 해도 max보다 작다면..
            return
        
    if n == 4:
        if maxV < Sum:
            maxV = Sum
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(n + 1, nx, ny, Sum + arr[nx][ny])
            dfs(n + 1, x, y, Sum + arr[nx][ny])  ## ㅗ ㅓ ㅏ ㅜ모양을 만드려면 
            visited[nx][ny] = 0                  ## x, y(제자리 탐색)를 다시 넘겨준다.

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maxV = 0
best = 0
for lst in arr:
    best = max(max(lst), best) ## 배열에서 가장 큰 숫자.. 백트래킹시 사용

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, i, j, arr[i][j]) ## ㅗ ㅏ ㅜ ㅓ를 제외한 모양
        visited[i][j] = 0
print(maxV)
## ㅗ ㅜ ㅏ ㅓ를 제외하고는
#    ㅁ
#  ㅁㅁㅁ
# ㅁㅁㅁㅁㅁ
#ㅁㅁㅁㅁㅁㅁ
# ㅁㅁㅁㅁㅁ
#   ㅁㅁㅁ
#     ㅁ
# 과 유사한 모양 안(ㅁ의 개수 무관.. 모양만 참조)에 모든 경우의 수가 포함된다.
# >> 따라서 한 점을 기준으로 4개씩 탐색하면 모든 도형의 경우를 포함하기 때문에
## 도형의 모양을 고려하지 않고 최댓값을 도출할 수 있다.
