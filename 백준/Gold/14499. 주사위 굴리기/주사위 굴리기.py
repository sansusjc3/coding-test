## 1 :동, 2 :서 3:북 4:남
dx = [0, 0, 0, -1, 1] ## n에 맞춰서..
dy = [0, 1, -1, 0, 0]
def game(n):
    global sx, sy
    nx, ny = sx+dx[n], sy+dy[n] ##n은 방향
    if 0 <= nx < N and 0 <= ny < M:
        if n == 1: #동
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif n == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif n == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        elif n == 4:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

## dice 변환 과정은 손가락 접어서 주사위마냥 돌려보자..

        if arr[nx][ny] > 0: ## 칸에 기입된 수가 0보다 크면
            dice[5] = arr[nx][ny] ## 주사위로 가져오고
            arr[nx][ny] = 0 ## 그 칸은 0
        else: ## 칸에 기입된 수가 0이면
            arr[nx][ny] = dice[5] ## 주사위 숫자를 그 칸으로
        sx, sy = nx, ny ## 만약 범위 안이라면.. 주사위는 구른 것이므로 시작점을 갱신해준다.
        return dice[0] ## 그리고 정상 수행했다면.. 윗면 리턴

    return -1 ## 범위 밖이라면.. -1 리턴

N, M, sx, sy, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0] * 6
for direct in order:
    res = game(direct) ## order에서의 방향을 인자로 넘겨주었다.
    if res >= 0: ## 정상 수행했을시는 return에 따라 윗면, 정상 수행 아닐시 -1 return 이므로..
        print(res)

## 윗면 0, 왼쪽 3, 오른쪽 2, 앞면 4 뒷면 1, 밑면 5(문제 예시 도면을 인덱스로 접근하였다)
## [0, 0, 0, 0, 0, 0]  #위 뒤 오 왼 앞 밑