import re

text = "This is the wednesday"
pick_word = r"wednesday"

search_word = re.search(pick_word , text)

if search_word:
    print("Word is present:" , search_word.group())
else:
    print("Word not present")