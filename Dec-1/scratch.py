import re

NUM_DICT = {
    "one": "1",
    "two" :"2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

STRING_LST = ["\d","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract_number_from_string(x):  
    string_parts = re.findall(r"(?=("+'|'.join(STRING_LST)+r"))", x)
    digits = [string_parts[0], string_parts[-1]]
    print(digits)
    translated_digits = [d if d.isdigit() else NUM_DICT.get(d) for d in digits ]
    return int(''.join(translated_digits))

with open ("Dec-1/input.txt") as f:
    lines = f.readlines()
    
total = 0

for line in lines:
    total += extract_number_from_string(line)

print(total)