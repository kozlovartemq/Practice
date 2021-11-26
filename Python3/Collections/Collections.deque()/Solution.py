from collections import deque
d = deque()
n = int(input())
for i in range(n):
    line, *args = input().split()
    getattr(d, line)(*args)       # getattr(x, 'y') is equivalent to x.y ( append 3 = d.append(3) )
print(' '.join(d))                # ' '.join(d) - paste together separate elements of 'd' with sep.: ' '
