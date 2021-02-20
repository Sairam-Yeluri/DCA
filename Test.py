lst = [2,8,4,3,4,6,7]

lst2 = []
l = len(lst)
k = 0
for i in range(l-1):
    if lst[i]<lst[i+1]:
        lst2.extend([lst[i],lst[i+1]])

print(lst2)
