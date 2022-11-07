N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort()
res = 0
cri_s, cri_e = arr[0][0], arr[0][1]

for i in range(1, N):
    if cri_e >= arr[i][0] and cri_e < arr[i][1]: ## 현재 시작점이 기준 끝점보다 작거나 같고, 현재 끝점이 기준 끝점보다 크다면..
        cri_e = arr[i][1]                         ## 쭉 이어갈 수 있다면...cri_e를 갱신하여 이어준다.

    elif arr[i][0] > cri_e: ## 현재 시작점이 기준 끝 점보다 클 때 == 선이 끊겼을 때
        res += cri_e - cri_s ## 여태껏 기록한 끝 - 시작으로 결과 더해주고
        cri_s, cri_e = arr[i][0], arr[i][1] ## 시작 끝 갱신
res += cri_e - cri_s ## 마지막 인덱스를 위함..
print(res)