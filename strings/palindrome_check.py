# Palindrome Check for a string

def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()  # remove spaces and lowercase
    return cleaned_text == cleaned_text[::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
