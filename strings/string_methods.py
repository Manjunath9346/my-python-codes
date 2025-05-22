text = "  Hello Python Developers  "

# strip() removes leading/trailing spaces
print("Stripped:", text.strip())

# split() splits by space (default) or custom separator
words = text.strip().split()
print("Words:", words)

# replace() replaces substrings
new_text = text.replace("Python", "Java")
print("Replaced:", new_text)

# find() returns index of first match or -1
pos = text.find("Python")
print("Position of 'Python':", pos)

# upper(), lower(), title()
print(text.upper())
print(text.lower())
print(text.title())
