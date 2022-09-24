x,y,z = map(int, input().split())
if x == 0:exit(print(0))
if   x > 0:
  if y < 0 or x < y:exit(print(x))
  if 0 < y < x:
    if y < z :exit(print(-1))
    else: 
      if z < 0:exit(print(abs(z)*2 + x))
      else:exit(print(x))
elif x < 0:
  if 0 < y or y < x:exit(print( abs(x) ))
  if x < y < 0:
    if z < y:exit(print(-1))
    else:
      if 0 < z:exit(print(abs(z)*2+ abs(x)))
      else:exit(print(abs(x)))