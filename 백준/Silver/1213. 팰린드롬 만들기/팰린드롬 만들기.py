alp = input()
N = len(alp)
info = dict()
cnt = 0
res = ''
alpha = []
for a in alp:
    if not info.get(a):
        info[a] = 1
    else:
        info[a] += 1

for key, value in info.items():
    if value % 2 == 1:
        cnt += 1
        if cnt >= 2:
            res = "I'm Sorry Hansoo"
            break
        res = key
        if value > 1:
            alpha.append(key)
            info[key] -= 1

    else:
        alpha.append(key)

alpha.sort(reverse=True)
for a in alpha:
    res = a*(info[a] // 2) + res + a*(info[a] // 2)
if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    print(res)