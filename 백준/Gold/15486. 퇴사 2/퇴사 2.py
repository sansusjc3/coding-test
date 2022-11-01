N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
    T, P = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i]) ## 해당일의 dp는 시작일까지의 수익과 비교하여 갱신
    if i+T-1 < N+1: ##시작 날 포함 T일간 이므로..
        dp[i+T-1] = max(dp[i-1]+P, dp[i+T-1]) ## 종료일의 dp는 (시작일까지의 수익+P)과 비교하여 갱신
print(dp[-1])