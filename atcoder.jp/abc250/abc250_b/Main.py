n,a,b = map(int,input().split()); s = '.';k = '#'; tmps = ''; tmpk = '';
lm = ''
ln = ''

for i in range(n):
  tmps = b * s
  tmpk = b * k
  if i%2 == 0:
    lm = lm + tmps
  else:
    lm = lm +tmpk
for i in range(n):
  tmps = b * s
  tmpk = b * k
  if i%2 == 0:
    ln = ln +tmpk
  else:
    ln = ln + tmps
for i in range (n):
  if i%2 == 0:
    for i in range(a):
      print(lm)
  else:
    for i in range(a):
      print(ln)