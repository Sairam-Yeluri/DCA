lst = [10,20,30,40,50,60]
rlst = [20,50,60,3]

for i in rlst:
    if i in lst:
        lst.remove(i)

print(lst)