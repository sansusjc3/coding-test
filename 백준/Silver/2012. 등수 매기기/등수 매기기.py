N = int(input())
result = [0]
for _ in range(N):
    result.append(int(input()))
result.sort()
res = 0
for i in range(1, N+1):
    res += abs(i-result[i])
print(res)