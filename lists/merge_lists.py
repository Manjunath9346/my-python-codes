# Merge Two Lists

# Merge two lists and remove duplicates
def merge_lists(list1, list2):
    merged = list1 + list2
    return merged

list1 = list(map(int, input("Enter first list (space-separated): ").split()))
list2 = list(map(int, input("Enter second list (space-separated): ").split()))

result = merge_lists(list1, list2)
print("Merged List:", result)
