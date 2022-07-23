ax,ay,bx,by = map(int, input().split())

if ay == bx:exit(print(0))
if by == ax:exit(print(0))
if bx < ax < ay < by:exit(print(ay-ax))
if ax < bx < by < ay:exit(print(by-bx))
if bx < ay <= by:exit(print(ay-bx))
if bx <= ax < by:exit(print(by-ax))
print(0)