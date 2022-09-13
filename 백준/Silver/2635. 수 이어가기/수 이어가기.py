N = int(input())

maxV = 0
result = []
for i in range(1, N+1):
    N_lst = [N]
    N_lst.append(i)
    j = 2
    while j<50000:
        n = N_lst[j-2] - N_lst[j-1]
        if n >= 0:
            N_lst.append(n)
            j += 1
        else:
            break
    cnt = len(N_lst)
    if cnt > maxV:
        maxV = cnt
        result = N_lst

print(maxV)
print(*result)