n,k,*a = map(int, open(0).read().split())
i = k
while i:
  i-=1;
  a[i::k]=sorted(a[i::k])
print('Yes' if a == sorted(a) else 'No')