import re

ark_schools = ["Globe", "Kings", "Elvin", "Victoria", "Bollingbroke"]
text = input("What school are you looking for? : ")

for pattern in ark_schools:
    print('Looking for "%s" in "%s" ->' % (text, ark_schools), end=' ')

    if re.search(pattern, text):
        print("found a match!")
    else:
        print("no match found")