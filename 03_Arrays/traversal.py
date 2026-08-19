marks = [88,95,34,51,44,1]

#Left to Right Traversal
for mark in marks:
    print(mark)

for i in range(len(marks)):
    print(marks[i])

#Right to Left Traversal
for mark in reversed(marks):
    print(mark)

for mark in marks[:-1]:
    print(mark)