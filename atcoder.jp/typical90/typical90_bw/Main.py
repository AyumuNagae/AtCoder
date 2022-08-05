n=int(input())
ans=0
d=0
for i in range(2,int(n**0.5)+1):
    while n%i==0:
        n//=i
        d+=1
if n !=1:
    d+=1
while 1<<ans<d:
    ans+=1 
print(ans)