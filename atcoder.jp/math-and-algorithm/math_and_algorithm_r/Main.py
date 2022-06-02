n = int(input())
a = list(map(int, input().split()))
a1 = a.count(100)
a2 = a.count(200)
a3 = a.count(300)
a4 = a.count(400)

print(a1*a4 + a2*a3)