s = {'a':input(),'b':input(),'c':input()}
n = 'a'

while len(s[n]) > 0:
  tmp = s[n][0]
  s[n] = s[n][1:]
  n = tmp
print(n.upper())