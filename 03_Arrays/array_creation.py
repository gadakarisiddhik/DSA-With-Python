# Array/List Creation
marks = [88,95,34,51,44,1] 

#Access O(1)
print(marks[0])
print(marks[2])
print(marks[-1])

#Insrt at end O(1)
marks.append(100)
print(marks)

#Insert at specific Position O(n)
marks.insert(2,55)
print(marks)

#Delete Last element O(1)
marks.pop()
print(marks)

#Delet by Index O(1)
marks.pop(1)
print(marks)

