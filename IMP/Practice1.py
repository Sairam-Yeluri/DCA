lst = [12,67,34]

l = len(lst)
lst1 = []

for i in range(l):
    for j in range(i+1,l):
        if lst[i]<lst[j]:
            k = lst[j]-lst[i]
            lst1.append(k)

print(max(lst1))

