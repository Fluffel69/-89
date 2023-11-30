x=input().split()
y=input().split()
ches=0
znam=0
if int(x[1])%int(y[1])==0 and int(y[1]) != int(x[1]):
    znam=int(x[1])
    ches=int(x[0])+(int(y[0])*int(x[1])%int(y[1])
elif int(y[1])%int(x[1])==0 and int(y[1]) != int(x[1]):
        znam=int(y[1])
        ches=int(y[0])+(int(x[0])*int(y[1])%int(x[1])
print(ches, znam)

