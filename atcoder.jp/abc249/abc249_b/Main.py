s = input()
if len(set(s)) != len(s) or s.isupper() or s.islower():
  print('No')
else:
  print('Yes')