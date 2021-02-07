lst = [1,2,3,{},{4,5},8]
print(lst)
lst2 = []
for i in lst:
    if i != {}:
        lst2.append(i)

print(lst2)