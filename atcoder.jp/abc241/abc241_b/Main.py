n,m = map(int, input().split())
a = list(map(int, input().split()))

for i in map(int, input().split()):
  if i in a:a.remove(i)
  else:exit(print("No"))
print("Yes")