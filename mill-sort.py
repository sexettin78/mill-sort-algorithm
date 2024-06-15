numbers = [81, 81, 99, 0, -1, 5, 3, 81, 0, 9, 10, 0, -5, 4, 2, 1, 91]
sorted_numbers = [None] * len(numbers)
usages = {}  
for j in numbers:
    if j in usages:
        usages[j] += 1
    else:
        usages[j] = 1
for j in numbers:
    smaller_count = 0
    equal_count = 0
    for i in numbers:
        if j < i:
            smaller_count += 1
        elif j == i:
            equal_count += 1
    sorted_numbers[len(sorted_numbers) - smaller_count - equal_count + usages[j] - 1] = j
    usages[j] -= 1
print(sorted_numbers)
