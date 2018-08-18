lst1 = []
maxnum = int(input("Number of Elements: "))
for i in range (1, maxnum+1):
    n = int(input("Element no. %d: " %(i)))
    lst1.append(n)

print("List has been successfully created.")
print(" ")
print("List 1: ", lst1)
print(" ")

lst2=['google','apple','facebook','microsoft','tesla']
lst1.extend(lst2)
print("Final List: ", lst1 )
