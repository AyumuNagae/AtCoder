N = int(input())
a = 1
a_mx = 0
while a ** 2 <= N:
    if N % a == 0:
        a_mx = a
    a += 1
print(max(len(str(a_mx)),len(str(N//a_mx))))