text = "I like apples and apples are tasty."
pattern = r"apples"

new_text = re.sub(pattern, "oranges", text)
print(new_text)
