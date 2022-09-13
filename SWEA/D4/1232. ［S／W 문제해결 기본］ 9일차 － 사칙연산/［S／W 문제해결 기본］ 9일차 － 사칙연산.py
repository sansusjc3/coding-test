## [S/W 문제해결 기본] 9일차 - 사칙연산
for tc in range(1, 11):
    N = int(input())
    tree = [0] + [input().split() for _ in range(N)]

    for i in range(N, 0, -1):
        if len(tree[i]) == 4:
            if tree[i][1] == '+':
                tree[i][1] = int(tree[int(tree[i][2])][1]) + int(tree[int(tree[i][3])][1])
            elif tree[i][1] == '-':
                tree[i][1] = int(tree[int(tree[i][2])][1]) - int(tree[int(tree[i][3])][1])
            elif tree[i][1] == '*':
                tree[i][1] = int(tree[int(tree[i][2])][1]) * int(tree[int(tree[i][3])][1])
            else:
                tree[i][1] = int(tree[int(tree[i][2])][1]) / int(tree[int(tree[i][3])][1])

    print(f'#{tc} {int(tree[1][1])}')