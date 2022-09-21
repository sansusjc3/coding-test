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
## 결과 값은 중복을 제외한 정렬 후 index
## set을 통해 중복제거 해준 후 딕셔너리에 좌표별 인덱스를 부여한다.
## 이후 input을 돌면서 print찍어준다.
