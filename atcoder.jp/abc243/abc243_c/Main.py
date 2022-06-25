n=int(input())
z=[list(map(int,input().split())) for _ in range(n)]
s=input();
[z[i].append(s[i]) for i in range(n)]
z.sort(key=lambda x:(x[1],x[0]))
for j in range(n-1):
    if z[j][1]==z[j+1][1] and z[j][2]=='R' and z[j+1][2]=='L':
        exit(print('Yes'))
print('No')