import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    elif command == 'size':
        print(len(que))
    elif command == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == 'empty':
        if que:
            print(0)
        else:
            print(1)
    else:
        command, num = command.split()
        que.append(num)