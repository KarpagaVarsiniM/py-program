
a = int(input("enter no of elements"))
list = []
for i in range (a):
        b = input("enter a letter")
        list.append(b)
tup = tuple(list)
print ("tuple",tup)
str= ""
for i in tup:
    str+=i

print ("string=",str)        
        
