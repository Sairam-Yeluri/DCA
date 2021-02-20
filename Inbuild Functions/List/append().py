lst = [1,2,3,4,5,6]

lst.append(7)
print(lst)      #[1, 2, 3, 4, 5, 6, 7]

lst.append([8,9])

print(lst)  #[1, 2, 3, 4, 5, 6, 7, [8, 9]]

lst.append({10,11})
lst.append([[12,13]])

print(lst)  #[1, 2, 3, 4, 5, 6, 7, [8, 9], {10, 11}, [[12, 13]]]

#lst.append(14,15)  wont work
