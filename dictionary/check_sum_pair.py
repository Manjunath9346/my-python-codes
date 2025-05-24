# Function to check if pair with given sum exists
def pair_sum(dict_store, arr, target_sum):
    for num in arr:
        complement = target_sum - num
        if complement in dict_store:
            return True
        dict_store[num] = True
    return False

def main():
    arr = [1, 2, 3, 3, 5]
    target = 8
    dict_store = {}  # Don't name it 'dict'

    if pair_sum(dict_store, arr, target) is True:
        return 'true'
    else:
        return 'false'

main()
