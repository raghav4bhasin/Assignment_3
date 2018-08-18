lst1 = []
maxnum = int(input("Number of Elements: "))
for i in range (1, maxnum+1):
    n = int(input("Element no. %d: " %(i)))
    lst1.append(n)
print(" ")
print("List has been successfully created.")
print(" ")
lst1.sort()
print("List 1: ", lst1)

