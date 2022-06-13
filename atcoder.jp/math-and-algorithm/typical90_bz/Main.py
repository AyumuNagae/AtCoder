n,m=map(int,input().split())
d=[0]*n
for _ in[0]*m:
  d[max(map(int,input().split()))-1]+=1
a = sum(i==1 for i in d)
print(a)