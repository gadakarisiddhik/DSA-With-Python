#O(n^2)
def has_duplicate_slow(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i !=j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [12,20,22,65,44,5,14,12]
result = has_duplicate_slow(numbers)

if result:
    print("Duplicate Found(Slow)")
else:
    print("Duplicate Not Found(Slow)")