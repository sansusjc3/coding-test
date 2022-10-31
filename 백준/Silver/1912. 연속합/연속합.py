N = int(input())
num = list(map(int, input().split()))
dp = num[::]
for i in range(1, N):
    dp[i] = max(dp[i], dp[i-1]+dp[i]) ## 그 인덱스의 값을 가져가는게 이득인지, 앞에것을 합해야 이득인지..
print(max(dp))
