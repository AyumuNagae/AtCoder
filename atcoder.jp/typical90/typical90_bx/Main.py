N=int(input())
A=list(map(int,input().split()))
n=sum(A)/10
A=A+A
s,l=0,0
for r in range(2*N):
    s+=A[r]
    if n<s:
        while n<s:
            s-=A[l]
            l+=1
    if s==n:exit(print("Yes"))
print("No")