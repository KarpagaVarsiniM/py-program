n = int(input(" enter the number of elements"))
I = list ()
for k in range (0,n):
        e = int(input("enetr the value"))
        I.append(e)
print ("original list :" ,I)
ascending = True
for i in range(len(I) - 1):
    if I[i] > I[i + 1]:
        ascending = False
        break

if ascending:
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
