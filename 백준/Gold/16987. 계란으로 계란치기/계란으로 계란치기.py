def egg(idx):
    global maxV
    if idx == N:
        res = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                res += 1
        maxV = max(maxV, res)
        return

    if eggs[idx][0] <= 0:
        egg(idx+1)

    else:   ## 시간 줄이기 else로 바꿔주면서 or  line 12에 return을 써주면서 다음 계란으로 넘어갔을 때 이 과정을 수행하지 않도록
        broken = 1
        for i in range(N):
            if idx != i and eggs[i][0] > 0:
                broken = 0
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                egg(idx+1)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
        if broken:
            egg(N)
## if로 해서 다 깨진 여부를 돌면서 체크하였는데,
## 어차피 돌아야 하는 for문 속에서 깨진 여부를 확인해주면서 시간을 줄인다....
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
egg(0)
print(maxV)