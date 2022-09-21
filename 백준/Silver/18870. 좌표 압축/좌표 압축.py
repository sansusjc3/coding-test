import sys
input = sys.stdin.readline
N = int(input())
xlst = list(map(int, input().split()))

index = sorted(list(set(xlst)))

info = {}
for i in range(len(index)):
    info[index[i]] = i

for k in range(N):
    print(info[xlst[k]], end = " ")