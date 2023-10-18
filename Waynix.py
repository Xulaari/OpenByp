# this is a project coded by swiss. credits to blukez for helping 

try:
    import pyperclip
except ImportError: # we know which import it is cause (its pretty self explanatory)
    import os
    os.system("pip install pyperclip -q")
    import pyperclip

# UNICODE IS ⁥

print("waynix v1.")

unicode = "⁥؍ہ"

simular_chars = {
    "a": "а",
    "c": "с",
    "e": "е",
    "j": "ј",
    "l": "ӏ",
    "s": "ѕ",
    "h": "һ",
    "v": "ν",
    "o": "о",
    "p": "р",
    "x": "х",
    "y": "у",
    "A": "Α",
    "B": "Β",
    "C": "С",
    "E": "Е",
    "N": "Ν",
    "I": "І",
    "M": "М",
    "O": "О",
    "H": "Н",
    "J": "Ј",
    "K": "Κ",
    "M": "Μ",
    "N": "Ν",
    "S": "Ѕ",
    "T": "Τ",
    "P": "Р",
    "X": "Χ",
    "Y": "Υ",
    "Z": "Ζ"
}

while True:
    string = list(input("enter to conv: "))

    convertedstring = ""

    for char in string:
        convertedchar = simular_chars.get(char, char)
        convertedstring += convertedchar

    endr = unicode.join(convertedstring)

    print(endr)

    pyperclip.copy(endr)
