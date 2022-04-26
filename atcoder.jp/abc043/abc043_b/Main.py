S = input()

ans = ''

for char in S:
    if char == 'B':
        ans = ans[:-1]
    elif char == '1':
        ans = ans + '1'
    elif char =='0':
        ans = ans + '0'

print(ans)