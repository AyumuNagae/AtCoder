X = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
 
d = dict()
for a,b in zip(X,alpha):
    d[a] = b
 
N = int(input())
 
def conv(s):
    ret = []
    for x in s:
        x = d[x]
        ret.append(x)
    return(''.join(ret))
 
 
S = [input() for i in range(N)]
S.sort(key = lambda x:conv(x))
for i in range(N):
    print(S[i])