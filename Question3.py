lst1 = []
maxnum = int(input("Number of Elements: "))
for i in range (1, maxnum+1):
    n = input("Element no. %d: " %(i))
    lst1.append(n)

print("List has been successfully created.")
print(" ")
print("List 1: ", lst1)
print(" ")

search = input("Object to be searched: ")
c = lst1.count(search)
if (c >= 1):
    print("Object '", search, "' occurs ", c, " times in the List.")

else:
    print("Object '", search, "' did not occur in the list.")
    
