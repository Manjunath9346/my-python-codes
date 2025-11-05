def countminreversals(s):
    n = len(s)
    if n % 2 != 0:
        return -1  # Odd length cannot be balanced

    stack = []
    for ch in s:
        if ch == '}' and stack and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(ch)

    # Count unbalanced opening and closing brackets
    open_count = stack.count('{')
    close_count = len(stack) - open_count

    # Each pair of unbalanced requires (open+1)//2 + (close+1)//2 reversals
    return (open_count + 1)//2 + (close_count + 1)//2
print(countminreversals("}{{}}{{{"))       #  Output: 3
print(countminreversals("{{}{{{}{{}}{{"))  #  Output: -1
print(countminreversals("{{{{"))           #  Output: 2
print(countminreversals("{{{{}}"))         #  Output: 1
print(countminreversals("{}{}"))           #  Output: 0
print(countminreversals("}{}{}{{"))        #  Output: 2
