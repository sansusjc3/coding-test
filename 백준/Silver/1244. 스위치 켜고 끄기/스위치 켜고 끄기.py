N = int(input())
button = [-1] + list(map(int, input().split()))
SN = int(input())
info = [list(map(int, input().split())) for _ in range(SN)]

for i in range(SN):
    gender, num = info[i][0], info[i][1]

    if gender == 1:
        k = 1
        while num * k <= N:
            if button[num * k] == 1:
                button[num * k] = 0
            elif button[num * k] == 0:
                button[num * k] = 1
            k += 1

    elif gender == 2:
        k = 0
        while num-k >= 0 and num+k <= N and button[num-k] == button[num+k]:
            if button[num-k] == 1:
                button[num-k], button[num+k] = 0, 0
            elif button[num-k] == 0:
                button[num-k], button[num+k] = 1, 1
            k += 1
for i in range(1, N+1):
    print(button[i], end = " ")
    if i % 20 == 0:
        print()
