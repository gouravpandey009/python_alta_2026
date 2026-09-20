# marks = [78 , 85 , 92 , 67 , 74]

# print("original Marks" , marks)

# append

# marks.append(88)
# print("After adding" , marks)

# insert

# marks.insert(3 , 45)
# print("After Inserting" , marks)

# remove

# marks.remove(85)
# print("After remove" , marks)

# sort

# marks.sort()
# print("Sorted Marks" , marks)

# print("Total students :" , len(marks))


# check existing marks

# print(85 in marks)

# print(100 not in marks)

# user search marks
marks = [78 , 85 , 92 , 67 , 74]

search = int(input("Enter marks to search"))

found = False

for mark in marks:
    if mark == search:
        found = True

if found:
    print("marks found")
else:
    print("marks not found")