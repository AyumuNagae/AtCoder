k = int(input())
a = int(k/60)
b = int(k%60)
c = 21+a
if b < 10:
  d = "0" + str(b)
else:
  d = str(b)
print(str(c)+":"+d)