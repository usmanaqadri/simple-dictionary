import json
from difflib import get_close_matches

word = input("Enter word: ")
data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        w = w.lower()
    if len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N for no. " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == 'n':
            return "That word doesn't exist"
        else:
            return "We didn't understand your entry"
    else:
        return "Not a word"

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
