lst = [5,20,-6,-4,1,3]
temp1  = lst[0]
for i in lst:
    if i < temp1:
        temp1 = i

temp2 = lst[0]
for j in lst:   
    if j > temp2:
        temp2 = j


print("Smallest number is {} and Largest number is {}".format(temp1,temp2))
