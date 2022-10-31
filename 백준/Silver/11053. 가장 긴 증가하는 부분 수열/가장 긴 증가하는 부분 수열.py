N = int(input())
num = list(map(int, input().split()))
dp = [1] * (N)
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if num[i] > num[j]: ## 증가 수열일 경우...
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))