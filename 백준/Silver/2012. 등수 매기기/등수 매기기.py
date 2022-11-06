N = int(input())
result = [0] ## 인덱스와 순위를 맞춰주기 위해 맨 앞에 하나 추가
for _ in range(N):
    result.append(int(input()))
result.sort()
res = 0
for i in range(1, N+1): ## 정렬한 배열을 돌면서 인덱스 - 순위의 절대값
    res += abs(i-result[i])
print(res)
