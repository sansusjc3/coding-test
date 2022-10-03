def paper(x,y,n):
    global res1, res2, res3
    cri = arr[x][y]
    for i in range(x, x+n): ## 전체 칸 탐색이지만 재귀에서 칸이 작아지기 때문에
        for j in range(y, y+n): # range(N)이 아닌 그에 맞는 조건을 넣어줘어야 한다..(신경쓰기)
            if arr[i][j] != cri: 
                for k in range(3):
                    for l in range(3):
                        paper(x + n//3 * k, y + n//3 * l, n//3)
                return
    if cri == -1:
        res1 += 1
    elif cri == 0:
        res2 += 1
    else:
        res3 += 1
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res1, res2, res3 = 0, 0, 0
paper(0,0,N)
print(res1)
print(res2)
print(res3)
## range 범위 생각할 때 싫증내지 않기..