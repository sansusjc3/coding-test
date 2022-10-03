def paper(x,y,n):
    global res1, res2
    cri = arr[x][y]
    for i in range(x, x+n): 
        for j in range(y, y+n): 
            if arr[i][j] != cri: 
                paper(x, y, n//2)
                paper(x + n//2, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y+n//2, n//2)
                return
    if cri == 0:
        res1 += 1
    else:
        res2 += 1
        
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res1, res2 = 0, 0
paper(0,0,N)
print(res1)
print(res2)
