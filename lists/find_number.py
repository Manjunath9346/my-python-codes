# finding the secong largest number in the list


def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]

print(second_largest([4, 1, 7, 7, 5, 9, 9]))
