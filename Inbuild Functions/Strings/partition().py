str1 = "abcdabcdabcd"

str2 = str1.partition("b")

print(str2) #('a', 'b', 'cdabcdabcd')

'''
Search for the word "match", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
'''