import sys
input = sys.stdin.readline

code = input().strip()
codeSize = len(code)
dp = [0 for _ in range(codeSize + 1)]

# 해독이 불가할 때
if code[0] == '0':
    print(0)

else:
    code = '0' + code
    dp[0], dp[1] = 1, 1

    for i in range(2, codeSize+1):
        # 0일 때는 앞이랑 세트라서 count X 이므로 0보다 클 때만
        if code[i] > '0':
            dp[i] += dp[i-1]
        # 두 개의 묶음은 두 자리 수이되, 범위 안이어야 한다
        if '10' <= code[i-1] + code[i] <= '26':
            dp[i] += dp[i-2]
    print(dp[codeSize] % 1000000)
