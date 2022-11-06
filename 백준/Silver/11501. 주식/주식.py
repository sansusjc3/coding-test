for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    cri = arr[-1]
    res = 0
    for i in range(N-2, -1, -1):
        if arr[i] >= cri:
            cri = arr[i]
        else:
            res += cri-arr[i]
## 역순으로 돌면서 기준 값보다 큰 값이 나오면 갱신, 작은 값이 나오면 결과에 더해준다.
