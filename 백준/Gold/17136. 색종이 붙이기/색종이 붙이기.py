def dfs(x, y, res):
    global minV

    if res > minV: ## 현재 붙인 개수가 이미 최소보다 크다면 return
        return

    if x == 10: ## 세로가 경계를 넘으면.. 최소 갱신
        if minV > res:
            minV = res
        return

    if y == 10: ## 가로가 경계를 넘으면.. 다음 줄 시작점으로
        dfs(x+1, 0, res)
        return

    if arr[x][y] == 1: ## 종이를 붙일 수 있는 칸이라면
        for p in range(5): 
            if paper[p] != 0 and x+p < 10 and y+p < 10: ## 종이를 쓸 수 있고, 배열 범위에 속하면
                stop = 0 ## (line25 참조)
                for i in range(x, x+p+1): ## 종이의
                    for j in range(y, y+p+1): ## 칸 수
                        if arr[i][j] == 0: ## 종이를 붙일 범위 안에 0이 하나라도 있으면
                            stop = 1  ## for문을 멈춘다.(stop은 line25 참조)
                            break
                    if stop: ## j가 정상 수행 됐을 때는 멈추면 안되므로 stop변수를 써주었다.(line19)
                        break
                if not stop: ## i의 반복문이 끝났는데 stop으로 나온게 아니라면(종이를 붙일 수 있다면)..
                    for i in range(x, x+p+1): 
                        for j in range(y, y+p+1):
                            arr[i][j] = 0 ## 붙여주고                 
                    paper[p] -= 1 ## 사용한 종이의 개수를 1장 빼준다.
                    dfs(x, y+1, res+1) ## 다음 칸으로 가고 종이는 붙였으므로 res+1로 호출
                    for i in range(x, x+p+1):
                        for j in range(y, y+p+1):
                            arr[i][j] = 1
                    paper[p] += 1   ## ((line33)~(line36)은 재귀의 복구)
    
    else: ## x, y칸이 종이를 붙일 수 없는 칸이라면
        dfs(x, y+1, res) ## 다음 칸 탐색 + 종이 안 붙였으므로 res로 호출(*res+1이 아니다)

arr = [list(map(int, input().split())) for _ in range(10)]
paper = [5] * 5 ## 각 5장씩 이므로...
minV = 26 ## (res 최악의 경우의 수 + 1) == (함수가 정상으로 끝났다면 나올 수 없는 값) 
dfs(0, 0, 0)    ## == res가 한번이라도 갱신됐다면 나올 수 없는 값
if minV != 26: ## 함수가 정상 수행 됐다면..
    print(minV) 
else: ## 정상 수행 안됐다면 == (minV 갱신이 없었다)
    print(-1)