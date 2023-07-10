
ls = []

for i in range(1,6):
    ls.append(int(input(f"Enter num{i} :")))

print(ls)

# calculating sum of all elements
print("Sum of all the elements is ",sum(ls))

# smallest element in list
print("Smallest element is ",min(ls))

# Largest element in list
print("Largest element is ",max(ls))

# List in ascending order
ls.sort()
print("List in ascending order is ",ls)

# List in descending order
ls.sort(reverse= True)
print("List in descending order is ",ls)

# Converting list in tuple
ls = tuple(ls)
print(ls)

# Deleting list(tuple)
del ls
print(ls)