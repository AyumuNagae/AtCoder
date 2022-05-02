import string
s=set(input())
s=sorted(s)
for i in string.ascii_lowercase:
  if not i in s:
    exit(print(i))
print("None")