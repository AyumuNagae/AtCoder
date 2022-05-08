ans = 4
h,w = map(int, input().split())
r,c = map(int, input().split())
if r == 1 or r == h:
  ans -= 1
if c == 1 or c == w:
  ans -= 1
if r == 1 & r == h:
  ans -= 1
if c == 1 & c == w:
  ans -= 1
print(ans)