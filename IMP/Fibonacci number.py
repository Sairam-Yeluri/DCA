
n = int(input("Enter number: "))
f = 0
s = 1
t = 0
if n==0:
    print(f)
elif n==1:
    print(f)
    print(s)
else:
    print(f)
    print(s)
    for i in range(2,n):
        t = f+s
        print(t)
        temp = s
        s = t
        f = temp

####################################################
#Nth Feb number:
a = 0
b = 1
if n < 0: 
    print("Incorrect input") 
elif n == 0: 
    print("{}th feb numer is {}".format(n,a))
elif n == 1: 
    print("{}th feb numer is {}".format(n,b)) 
else: 
    for i in range(2,n): 
        c = a + b 
        a = b 
        b = c 
    print("'{}' feb numer is {}".format(n,b)) 
 
###############################################
#Check whether feb or not:
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print(n,"Yes")
    else:
        print(n,"No")