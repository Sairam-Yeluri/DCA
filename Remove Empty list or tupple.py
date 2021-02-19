lst = [10,20,[1,2],[],30,{},{4,5},40]
lst2 = []
print("Original list is {}".format(lst))
for i in lst:
    if i!= []:
        lst2.append(i)

print("Removed list is {}".format(lst2))

lst3 = []
for i in lst:
    if i != {}:
        lst3.append(i)

print("Removed tuple is {}".format(lst3))
