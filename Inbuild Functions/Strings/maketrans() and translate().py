str1 = "Hello Sam How are you!"
str2 = str1.maketrans("S", "R")
print(str1.translate(str2)) #Hello Ram


str3 = str1.maketrans("S", "R",'Hell') 
print(str1.translate(str3)) #o Ram ow ar you! (Removes 'H','e','l','l')