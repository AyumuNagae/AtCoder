s = input(); t = input();
print('Yes'if sorted(s) < sorted(t, reverse=True) else 'No')