lst3 = []
str = 'sr51sa76'
lst = list(str)
lst.remove('5')
print(lst)
lst2 = "".join(lst)
print(lst2)
for i in range(len(lst2)-1):
    if lst2[i]!='7' and lst2[i+1]!='6':
        lst3.append(lst2[i])
        

lst4 = "".join(lst3)
print(lst4)

