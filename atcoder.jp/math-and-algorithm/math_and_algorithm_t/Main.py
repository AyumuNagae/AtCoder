n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
	for j in range(i):
		for k in range(j):
			for l in range(k):
				for m in range(l):
					if a[i]+a[j]+a[k]+a[l]+a[m]==1000:
						ans+=1
print(ans)