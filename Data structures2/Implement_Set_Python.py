# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    s.add(element)


# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    s.discard(element)   # safe remove (no error)


# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    return sum(s)
s = set()
insert(s, 5)
insert(s, 10)
remove_from_set(s, 5)
print(sum_set(s))   # Output → 10
