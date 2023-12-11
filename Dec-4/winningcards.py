import math
import re

def parse_line(game):
    matches = 0
    winning_nums = []
    our_nums = []
    winning_nums = game.split('|')[0]
    winning_nums = list(re.findall(r"\d+", winning_nums))[1:]
    our_nums = game.split('|')[1]
    our_nums = list(re.findall(r"\d+", our_nums))
    for number in our_nums:
        if number in winning_nums:
            matches += 1
    # Decrease by one to appropriately double
    return matches

def main():
    with open('Dec-4/input.txt') as f:
        lines = f.readlines()
    total_scratch_cards = len(lines)
    output_arr = [parse_line(game) for game in lines]
    # Loop through our array of matches. If we have more than 0 matches, go to the next x cards and create a copy (where x is the number of matches)
    for i in range(0, len(output_arr)):
        if output_arr[i] > 0:
            total_scratch_cards += output_arr[i]
            # If we have more than 0 matches. Double 
            try:
               for j in range(i + 1, i + output_arr[i] + 1):
                output_arr[j] = output_arr[j] * 2
            except IndexError:
                pass
            
            
    # total_scratch_cards = sum(output_arr)
    print(sum(output_arr))

if __name__ == "__main__":
    main()