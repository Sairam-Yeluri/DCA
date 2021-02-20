lst = [2,8,4,3,4,6,6,2]
lst2 = []
l = len(lst)
k,p = 0,0
for i in range(l-1):
    
    if lst[i]<lst[i+1]:
        k = k+lst[i]
        p = p+1
        if i == l-2 and p!=0:
            d = k+lst[i+1]
            lst2.append(d)
    else:
        if p!= 0:
            d = k+lst[i]
            lst2.append(d)
            k=0
            p = 0

print(lst2)