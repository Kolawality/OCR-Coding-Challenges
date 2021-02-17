import re

user_text = input("Please enter your text: ")
p = re.compile(user_text)

search_key = input("Please enter the word you wish to search for: ")
m = p.match(search_key)

if m:
    print("Match found: ", m.group())
else:
    print("No match")