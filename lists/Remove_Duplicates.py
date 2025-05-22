#  Remove Duplicates without using set
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
