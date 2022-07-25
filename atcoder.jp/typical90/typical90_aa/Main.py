users = set()
for i in range(1, int(input())+1 ):
  name=input()
  if name not in users:
    users.add(name)
    print(i)