import re

text = "This is the wednesday"
split_text = r" "

split_text_result = re.split(split_text , text)

print("Split result:" , split_text_result)