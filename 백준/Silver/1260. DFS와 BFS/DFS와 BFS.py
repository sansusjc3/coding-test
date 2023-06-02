import sys
from collections import deque
def dfs(idx):
    global visited
    visited[idx] = 1
    print(idx, end=" ")
    for nextIdx in range(1, N+1):
        if not visited[nextIdx] and graph[idx][nextIdx]:
            dfs(nextIdx)

def bfs(idx):
    global q, visited
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for nextIdx in range(1, N+1):
            if not visited[nextIdx] and graph[cur][nextIdx]:
                q.append(nextIdx)
                visited[nextIdx] = 1

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(V)
print()
visited = [0] * (N+1)
q = deque()
q.append(V)
visited[V] = 1
bfs(V)