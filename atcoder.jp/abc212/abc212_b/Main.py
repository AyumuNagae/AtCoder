a = input()
if a[0] == a[1] == a[2] == a[3]:exit(print("Weak"))
elif a in "0123456789012":print("Weak")
else:print("Strong")