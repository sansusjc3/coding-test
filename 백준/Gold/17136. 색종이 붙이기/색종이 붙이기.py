def dfs(x, y, res):
    global minV

    if res > minV:
        return

    if x == 10:
        if minV > res:
            minV = res
        return

    if y == 10:
        dfs(x+1, 0, res)
        return

    if arr[x][y] == 1:
        for p in range(5):
            if paper[p] != 0 and x+p < 10 and y+p < 10:
                stop = 0
                for i in range(x, x+p+1):
                    for j in range(y, y+p+1):
                        if arr[i][j] == 0:
                            stop = 1
                            break
                    if stop:
                        break
                if not stop:
                    for i in range(x, x+p+1):
                        for j in range(y, y+p+1):
                            arr[i][j] = 0                  
                    paper[p] -= 1
                    dfs(x, y+1, res+1)
                    for i in range(x, x+p+1):
                        for j in range(y, y+p+1):
                            arr[i][j] = 1
                    paper[p] += 1
    
    else:
        dfs(x, y+1, res)

arr = [list(map(int, input().split())) for _ in range(10)]
paper = [5] * 5
minV = 26
dfs(0, 0, 0)
if minV != 26:
    print(minV)
else:
    print(-1)