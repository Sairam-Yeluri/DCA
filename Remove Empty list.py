lst = [10,20,[1,2],[],30]
lst2 = []
print("Original list is {}".format(lst))
for i in lst:
    if i!= []:
        lst2.append(i)

print("New list is {}".format(lst2))