def dfs(idx, n):
    global minV
    if n == M: ## 남겨둘 치킨집의 개수가 됐을 때
        res = check_distance() ## 거리 확인 함수를 호출(dis(밑 함수 참조)가 return됨)
        minV = min(minV, res) ## 거리 확인 함수의 결과와 minV의 비교
        return
    for i in range(idx, len(tmp)): ##조합하고
        comb.append(tmp[i])
        dfs(i+1, n+1)
        comb.pop()

def check_distance():
    dis = 0 ## d(한 집에서 가장 가까운 치킨집과의 거리)를 누적하는 변수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: ## 집이라면
                d = 100
                for k in range(M): ## 치킨집 후보 중, 어느 집이 제일 가깝나 확인하기 위해
                    d = min((abs(comb[k][0] - i) + abs(comb[k][1] - j)), d) #최소를 뽑고
                dis += d ##총 거리에 누적해준다
    return dis ## d(한 집에서 가장 가까운 치킨집과의 거리)를 누적하는 변수 리턴

N, M = map(int, input().split()) ## N(가로,세로) M(폐업 안 할)
arr = [list(map(int, input().split())) for _ in range(N)]
#r,c는 1부터
minV = 100000
tmp = [] ##모든 치킨집의 좌표를 담을 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: ##치킨집이면
            tmp.append((i, j)) ## 넣어준다

comb = [] ## 치킨집(tmp) 조합할 빈 배열..(dfs함수에서 사용 예정)
dfs(0,0)
print(minV)
