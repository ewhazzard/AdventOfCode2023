import regex as re

def word_to_num(input_word):
    if input_word == 'one':
        return '1'
    elif input_word == 'two':
        return '2'
    elif input_word == 'three':
        return '3'
    elif input_word == 'four':
        return '4'
    elif input_word == 'five':
        return '5'
    elif input_word == 'six':
        return '6'
    elif input_word == 'seven':
        return '7'
    elif input_word == 'eight':
        return '8'
    elif input_word == 'nine':
        return '9'
    elif input_word == 'ten':
        return '10'
    else:
        return input_word
    
STRING_LST = ["\d","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]    

def parse_line(input_line):
    digits_in_input = re.findall(r"(?=("+'|'.join(STRING_LST)+r"))", input_line)
    first_digit = digits_in_input[0]
    second_digit = digits_in_input[-1]
    first_digit = word_to_num(first_digit)
    second_digit = word_to_num(second_digit)
    print(input_line)
    print(digits_in_input)
    print(int(first_digit + second_digit))
    return int(first_digit + second_digit)

def main():
    with open('Dec-1/input.txt') as f:
        lines = f.readlines()
    output_arr = [parse_line(line) for line in lines]
    answer = sum(output_arr)
    print(answer)

if __name__ == "__main__":
    main()
    