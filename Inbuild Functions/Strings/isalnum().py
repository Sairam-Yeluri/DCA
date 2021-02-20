str1 = '123'    #T
str2 = 'sai'    #T
str3 = 'sai123' #T
str4 = 'sai 123'    #Space is not alnum so F
print(str1.isalnum(),str2.isalnum(),str3.isalnum(),str4.isalnum())
str = 123
#Wont work as str (123) is num