lst = [1,2,3,4,5,6,7,8,9]
n = 3
l = len(lst)
def chunk(lst, n): 
  
  for i in range(0, l, n): 
    yield lst[i:i + n]

x = list(chunk(lst,n))
print(x)

k = []
for i in range((l + n - 1) // n ) :
    k.append(lst[i * n:(i + 1) * n] )
print(k)