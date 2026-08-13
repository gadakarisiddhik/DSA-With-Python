#O(n) = (O.n)
def has_duplicate_fast(numbers):
    seen = set() #tuple
    for number in numbers:
        if number in seen: 
            return True
        seen.add(number)
    return False

numbers = [12,20,22,65,44,5,14,1]
result = has_duplicate_fast(numbers)

if result:
    print("Duplicate Found(Fast)")
else:
    print("Duplicate Not Found(Fast)")