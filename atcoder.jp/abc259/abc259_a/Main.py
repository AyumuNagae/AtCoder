now,moment,x,tall,diff = map(int, input().split())
origin = tall - x*diff
ans = moment*diff+origin
if moment >= x:
  print(tall)
else:
  print(ans)