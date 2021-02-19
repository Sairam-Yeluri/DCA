lst = [1,2,2,3,4,5,5,6]
st = list(set(lst))
dup = []
for i in st:
    if lst.count(i)>1:
        dup.append(i)

print(dup)