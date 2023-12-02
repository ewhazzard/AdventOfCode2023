import regex as re

red_cubes = 12
green_cubes = 13
blue_cubes = 14

def find_power_of_set(game_input):
    
    min_red_needed = 1
    min_green_needed = 1
    min_blue_needed = 1
    
    all_reds = re.findall(r'\d{1,2} red', game_input)
    all_red_nums = [int(pull[:2].strip()) for pull in all_reds]
    for num in all_red_nums:
        if num > min_red_needed:
            min_red_needed = num
    
    all_blues = re.findall(r'\d{1,2} blue', game_input)
    all_blue_nums = [int(pull[:2].strip()) for pull in all_blues]
    for num in all_blue_nums:
        if num > min_blue_needed:
            min_blue_needed = num
        
    all_greens = re.findall(r'\d{1,2} green', game_input)
    all_green_nums = [int(pull[:2].strip()) for pull in all_greens]
    for num in all_green_nums:
        if num > min_green_needed:
            min_green_needed = num
    return min_red_needed * min_blue_needed * min_green_needed

def is_possible_game(game_input):
    
    all_reds = re.findall(r'\d{1,2} red', game_input)
    all_red_nums = [int(pull[:2].strip()) for pull in all_reds]
    for num in all_red_nums:
        if num > red_cubes:
            return False
    
    all_blues = re.findall(r'\d{1,2} blue', game_input)
    all_blue_nums = [int(pull[:2].strip()) for pull in all_blues]
    for num in all_blue_nums:
        if num > blue_cubes:
            return False
        
    all_greens = re.findall(r'\d{1,2} green', game_input)
    all_green_nums = [int(pull[:2].strip()) for pull in all_greens]
    for num in all_green_nums:
        if num > green_cubes:
            return False
    return True

def parse_game(game):
    # game_id = game[4:8].strip(' :')
    # if is_possible_game(game):
    #     return int(game_id)
    # return 0
    return find_power_of_set(game)

def main():
    with open('Dec-2/input.txt') as f:
        lines = f.readlines()
    output_arr = [parse_game(game) for game in lines]
    answer = sum(output_arr)
    print(answer)

if __name__ == "__main__":
    main()