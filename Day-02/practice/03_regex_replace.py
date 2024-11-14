import re

text = "This is the wednesday"
pick_word = r"wednesday"

print("Old text is:" , text)

replace_word = "sunday"

new_text = re.sub(pick_word , replace_word , text)

print("New text is:" , new_text)