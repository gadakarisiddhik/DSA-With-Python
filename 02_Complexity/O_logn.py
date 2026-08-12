def find_name(names,target):
    left = 0
    right = len(names)-1

    while left <= right:
        middle = (left+right) // 2

        if names[middle] == target:
            return middle

        elif names[middle] < target:
            left = middle + 1

        else:
            right = middle + 1

    return -1

names = ["Pooja","Rushikesh","Siddik","Tipu","Umar","Ved"]
key = "Siddik"

result = find_name(names,key)