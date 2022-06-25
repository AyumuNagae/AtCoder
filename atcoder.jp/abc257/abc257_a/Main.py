n, x = map(int, input().split())
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = x//n -1
if x%n != 0:b+=1
print(abc[b])