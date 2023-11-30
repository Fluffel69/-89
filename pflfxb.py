x = input().split()
y = input().split()
c = 0
z = 0
if int(x[1]) % int(y[1]) == 0 and int(y[1]) != int(x[1]):
    z = int(x[1])
    c = int(x[0])+(int(y[0])*(int(x[1]) // int(y[1])))
elif (int(y[1]) % int(x[1]) == 0) and (int(y[1]) != int(x[1])):
    z = int(y[1])
    c = int(y[0])+(int(x[0]) * (int(y[1]) // int(x[1])))
print(c, z)
