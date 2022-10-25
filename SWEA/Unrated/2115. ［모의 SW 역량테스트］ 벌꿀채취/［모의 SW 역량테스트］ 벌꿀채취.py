def dfs(idx, honey, honeyV): ##(체크 중인 인덱스, C랑 비교할 꿀양, 수익(꿀**2))
    global maxV
    if honey > C:
        return
 
    if idx == M:
        maxV = max(maxV, honeyV)
        return
 
    dfs(idx+1, honey, honeyV) ## 안 넣고
    dfs(idx+1, honey+bowl[idx], honeyV+bowl[idx]**2) ## 넣고 (부분 집합으로 접근하였다.)
 
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * (N-M+1) for _ in range(N)] ## result는 그 지점을 시작으로 최대값을 넣을 배열(이 생각이 핵심인듯..)
    for i in range(N):
        for j in range(N-M+1):
            maxV = 0
            bowl = arr[i][j:j+M] ##일꾼이 가질 수 있는 통만큼 잘라서
            dfs(0, 0, 0) ## 돌려용
            result[i][j] = maxV ##[i][j]를 시작으로 M개의 범위에서 최대인 경우를 넣어준다.
 
    res = 0 ##최대 수익을 담을 변수
    if M*2 <= N: ## 일꾼의 수 * 통이 배열보다 작다면(== 한 줄에 두 명이 일 할 수 있다면)
        for i in range(N): #행
            for j in range(N-2*M+1): # 첫 번째 일꾼은 최대(원래의 범위(N-M+1)에서 두 번째 일꾼의 범위(M)를 뺀 만큼)
                for k in range(j+M, N-M+1): # 두 번째 일꾼은 첫 놈이 일 한 곳 다음부터 배열 속 통을 집어넣을 수 있는 최대 열까지
                    res = max(res, result[i][j] + result[i][k]) ## j와 k로 모든 경우에 접근하여 최대를 도출한다.
    row = [] ## 행이 다를 경우...
    for r in result: ## 최댓값 결과를 넣은 이차원 배열(result) 속 1차원 배열에 접근해서..(== 행에 접근해서)
        row.append(max(r)) ## 최대를 찾은 후 row(행 별 최대를 넣을 배열)에 넣어준다.
    row.sort() ## 정렬 후
    res = max(res, row[-1] + row[-2]) ## 1. 제일 큰 값(일꾼1) + 다음 큰 값(일꾼2)
    print(f'#{tc} {res}')             ##  2. max(line35, 같은 행에서 일 할 수 있는 경우의 최대)를 통해
                                      ## 최종 결과를 도출한다.
