import json
import difflib
# from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    original = word
    word = word.lower()
    if word in data: 
        return data[word]
    elif word.title() in data:
        return data[word.title()]    
    elif word.upper() in data: 
        return data[word.upper()]
    elif original in data: 
        return data[original] 
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y for yes, n for no. " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist! Please double check it."
        else: 
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist! Please double check it."

word = input("Enter Word: ")
output = translate(word)

if type(output) == list:
    for item in output: 
        print(item)
else: 
    print(output)
