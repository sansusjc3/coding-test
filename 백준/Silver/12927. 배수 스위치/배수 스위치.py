button = ['']+list(input())
N = len(button)
cnt = 0
for i in range(1, N):
    if button[i] == 'Y':
        for j in range(i, N, i):
            if button[j] == 'Y':
                button[j] = 'N'
            else:
                button[j] = 'Y'
        cnt += 1
print(cnt)