##3^0 * 3^0 일 때 *
## 3^1 * 3^1 일 때 >> 가운데 비우고 3^0으로 채우기
## 3^2 * 3^2 일 때  >> 가운데 비우고 3^1로 채우기..
def erase(x, y, n):
    if n == 1:
        return
    for i in range(x+n//3, x+n//3*2): ## 각 영역별로 x,y 좌표의 시작은 길이를 3등분한 시작부터
        for j in range(y+n//3, y+n//3*2): ## 3등분한 끝 -1 까지이다. range로 넣어주기 때문에 
            arr[i][j] = ' '                ## 1/3 ~ 2/3으로 표현 가능하다.
    ## 별 지워줬으면        
    for k in range(3): ## 9등분 해준다.
        for l in range(3):
            erase(x+n//3*k, y+n//3*l, n//3)

N = int(input())
arr = [['*' for _ in range(N)] for _ in range(N)]
erase(0, 0, N)
for a in arr:
    print(''.join(a))
