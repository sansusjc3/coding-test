N = int(input())
num = list(map(int, input().split()))
dp = [0] * (N+1)
dp[0] = num[0]

for i in range(1, N):
    for j in range(i):
        if num[i] > num[j]: ## 증가 수열일 경우...
            dp[i] = max(dp[i], dp[j] + num[i])
        else: ## 증가 수열이 아닐 때는 단일값을 넣어주어야 한다.(그렇지 않으면 초기값 0이 그대로..)
            dp[i] = max(dp[i], num[i])

print(max(dp))