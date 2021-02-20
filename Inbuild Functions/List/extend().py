lst = [1,2,3,4]

lst.extend([5,6])
print(lst)  #[1, 2, 3, 4, 5, 6]

lst.extend({7,8})
print(lst)  #[1, 2, 3, 4, 5, 6, 8, 7]

lst.extend((9,10))
print(lst)  #[1, 2, 3, 4, 5, 6, 8, 7, 9, 10]

#Wont take 2 args