lst = [10,20,30,40,50]
n = int(input("Enter the rotation: "))
print("Original List is:",lst)
l = len(lst)
l1 = lst[0:n]
l2 = lst[n:l]
lst2 = l2+l1

print("{} left rotated list is {}".format(n,lst2))
