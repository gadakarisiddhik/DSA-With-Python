#Right to Left Traversal Using Neasted Loop O(n**2)
classroom = [
    [85,89,78], #r0
    [72,88,91], #r1
    [95,60,83], #r2
]

for row in classroom:
    for marks in row:
        print(marks,end=" ")
    print()