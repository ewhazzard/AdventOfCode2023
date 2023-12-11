import re
import math

def is_valid_game(distance, total_time, held_time):
    # The speed of the boat * the remaining time must > distance to win the race
    if held_time * (total_time-held_time) > distance:
        return True
    return False

def find_possible_games(total_time, distance):
    print(total_time, distance)
    possibilities = 0
    for hold_time in range (0, total_time):
        if is_valid_game(distance, total_time, hold_time):
            possibilities += 1
    return possibilities
            

def main():
    with open('Dec-5/input.txt') as f:
        lines = f.readlines()
    times = re.findall('\d+', lines[0])
    distances = re.findall('\d{1,4}', lines[1])
    race_dict = {}
    output = []
    for i in range(0, len(times)):
        race_dict[times[i]] = distances[i]
    for race in race_dict:
        output.append(find_possible_games(int(race), int(race_dict[race])))
    print(math.prod(output))
    
def main_2():
    with open('Dec-5/input.txt') as f:
        lines = f.readlines()
    times = re.findall('\d+', lines[0])
    distances = re.findall('\d{1,4}', lines[1])
    time_str, distance_str = '', ''
    for time in times:
        time_str += time
    for distance in distances:
        distance_str += distance
    print(find_possible_games(int(time_str), int(distance_str)))

if __name__ == "__main__":
    main()
    main_2()