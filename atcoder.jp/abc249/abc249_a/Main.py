a,b,c,d,e,f,x = map(int,input().split())
takahashi = 0
aoki = 0


for t in range(x):
    if t%(a+c)<a:
        takahashi+=b
    if t%(d+f)<d:
        aoki+=e

if takahashi>aoki:
    print('Takahashi')
elif aoki>takahashi:
    print('Aoki')
else:
    print('Draw')
