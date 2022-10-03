def paper(x,y,n):
    global res
    cri = arr[x][y]
    for i in range(x, x+n): 
        for j in range(y, y+n): 
            if arr[i][j] != cri: ## 색이 다르면 나눠야한다.
                res += '(' ## 나눌 때 열고
                paper(x, y, n//2)
                paper(x, y+n//2, n//2)                
                paper(x + n//2, y, n//2)
                paper(x+n//2, y+n//2, n//2)
                res += ')' ## 다 끝내면 닫는다.
                return
    res += cri ## for문이 멈추지 않았으면 >> 일치한다는 소리로 압축


N = int(input())
arr = [list(input()) for _ in range(N)]
res = ''
paper(0,0,N)
print(res)