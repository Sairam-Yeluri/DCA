lst = [1,'a',2,'b',3,'c',4]
temp = 0
for i in lst:
    if str(i).isnumeric():  #Int dont have this function
        temp = temp+i

print(temp)