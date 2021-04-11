str1 = 'morning'
str2 = 'bring'
lst1 = list(str1)
lst2 = list(str2)
k = []
for i in lst1:
    if i not in lst2:
        k.append(i)

st1 = set(lst1)
ln = len(lst1)-len(st1)

print(len(k)+ln)