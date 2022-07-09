s, t, x = map(int, input().split())
if s < t:
  ans = s <= x < t 
else:
  ans = s <= x or x < t
print('Yes' if ans else 'No')