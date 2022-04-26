n, k = list(map(int,input().split()))
d_s = list(map(int,input().split()))
a = n
while True:
    t = True
    for d in d_s:
        if str(d) in str(a):
            t = False
    if t:
        print(a)
        exit()
    else:
        a += 1