a  = list(map(int, input().split()))
ppap = {}
for i in a:
  if i in ppap:ppap[i] += 1
  else: ppap[i] = 0
if list(ppap.values()) == [2,1] or list(ppap.values()) == [1,2]:print("Yes")
else:print("No")