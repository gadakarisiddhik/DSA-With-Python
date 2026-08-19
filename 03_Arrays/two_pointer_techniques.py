def find_two_numbers(numbers,target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        Total = numbers[left] + numbers[right]

        if Total == target:
            return [numbers[left],numbers[right]]
        
        elif Total > target:
            right -= 1

        else:
            left -= 1
    return []
        
numbers = [1,3,5,6,8,11]
print(find_two_numbers(numbers,14))
