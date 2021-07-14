t = int(input())
a = int(input())
b = int(input())
s = []
s.append(a)
s.append(b)
print(a)
print(b)
for i in range(2, t):
    x = s[i-1]
    y = s[i-2]
    s.append(x + y)
    print(x + y)
