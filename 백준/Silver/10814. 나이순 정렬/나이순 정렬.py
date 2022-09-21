import sys
input = sys.stdin.readline
N = int(input())
member = [input().split() for _ in range(N)]
member.sort(key=lambda x:int(x[0]))

for i in range(N):
    print(*member[i])
##2 1과 같은 코드에 import만 했는데 무난.. 무슨 차이

## 람다 표현식 
#  >> plus_ten = lambda x: x+10   매개변수 : 식
#1  >> plus_ten(1) >> 11
#2 >> (lambda x: x+10)(1) >> 11 둘다 사용 가능하다..
# sort,sorted에는 key가 존재한다
# 별도로 지정 안해주면 기본 순서대로 우선순위 할당이며,, key = ㅁ 해주면 그 순서대로 정렬한다. 
## 문제에서 그냥 sorted로만 할 경우 나이가 동갑일 경우 정렬을 위해 이름의 순서까지 접근 해버리므로
## 별도의 key를 할당해서 나이가 같을 경우 입력된 순서대로 출력되게 한다.



## 오답 코드
# N = int(input())
# member = []
# for _ in range(N):
#     age, name = input().split()
#     age = int(age)
#     if member:
#         for i in range(len(member)):
#             if age < member[i][0]:
#                 member.insert(i, [age, name])
#                 break
#             elif age == member[i][0]:
#                 member.insert(i+1, [age, name])
#                 break
#     else:
#         member.append([age, name])

# for i in range(N):
#     print(*member[i])
# 0 원래 코드.. 시간초과 수업 때 한 정렬로 되나??
#  딕셔너리로 하려 했는데 key 중복
#  value로 하면 비효율적 
