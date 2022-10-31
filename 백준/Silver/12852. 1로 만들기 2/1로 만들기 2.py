N = int(input())
dp = [[0, []] for _ in range(N+1)]
dp[1][0] = 0
dp[1][1] = [1]
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]
    if i%2 == 0 and dp[i//2][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]
    if i%3 == 0 and dp[i//3][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
print(dp[-1][0])
print(*dp[-1][1][::-1])

## 다이나믹 프로그래밍 >> 메모이제이션 + 점화식 기억하자..(코드 참조..)