import re

text = "This is the wednesday"
pick_word = r"wednesday"

match = re.match(pick_word , text)

if match:
    print("Word Matched:" , match.group())
else:
    print("Word not Match")