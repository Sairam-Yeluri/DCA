n = int(input("Enter Number: ")) #153 , 154
lst = list(str(n))
k = 0
for i in lst:
    k = k+pow(int(i),3)

if k == n:
    print("Yes")
else:
    print("No")

