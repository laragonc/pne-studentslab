a = 0
b = 1
print(a)
for i in range(11):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

