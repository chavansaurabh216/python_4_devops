import re

text = "This is the wednesday"
pick_word = r"wednesday"

search = re.search(pick_word , text)

if search:
    print("Pattern Found:" , search.group())
else:
    print("Pattern Not Found")