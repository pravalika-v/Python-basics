# find the largest number
'''numbers = [4, 8, 9, 10, 49, 5]
large = 0
for i in numbers:
        if i > large:
            large = i
print (large)'''
#to remove duplicates in the list
numbers = [4, 5, 8, 19, 4, 7, 8]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)
