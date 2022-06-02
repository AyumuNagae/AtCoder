n = int(input())
for i in range(2,int(n**0.5)):
  if n%i==0:
    print('No')
    exit()
print('Yes')