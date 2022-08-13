s = [input() for i in range(3)]
t = input()
a = ""
for i in t:
  i = int(i)
  i-=1
  a= a+s[i]
print(a)