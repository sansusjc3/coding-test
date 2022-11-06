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
    print(res)