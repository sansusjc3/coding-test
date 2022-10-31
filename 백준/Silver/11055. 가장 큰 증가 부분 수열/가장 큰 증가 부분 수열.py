N = int(input())
num = list(map(int, input().split()))
dp = [0] * (N+1)
dp[0] = num[0]

for i in range(1, N):
    for j in range(i):
        if num[i] > num[j]: ## 증가 수열일 경우...
            dp[i] = max(dp[i], dp[j] + num[i])
        else: ## 증가 수열이 아닐 때는 단일값과 현재까지의 dp(그 전 증가수열이었을 인덱스 때 넣어둔 값)를 비교한다.
            dp[i] = max(dp[i], num[i]) ## 아무 비교도 없을 시 초기 할당한 0 이 그대로..

print(max(dp))