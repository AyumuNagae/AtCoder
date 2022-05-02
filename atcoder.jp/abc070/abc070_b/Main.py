a,b,c,d = map(int,input().split())

ac=max(a,c)
bd=min(b,d)

print(max(0,bd-ac))