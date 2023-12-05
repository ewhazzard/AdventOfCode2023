import numpy as np

def get_entire_num(input_matrix, row_idx, col_idx):
    result = input_matrix[row_idx][col_idx]
    # Iterate to the left and add to the beginning of the result
    for i in range(col_idx - 1, 0, -1):
        if input_matrix[row_idx][i].isdigit():
            result = input_matrix[row_idx][i] + result
        else:
            break
    for j in range(col_idx + 1, len(input_matrix[row_idx])):
        if input_matrix[row_idx][j].isdigit():
            result = result + input_matrix[row_idx][j]
        else:
            break
    return result

def adjacent_values(input_matrix, row_idx, col_idx):
    moves = [(-1,-1), (-1,-0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for move in moves:
        try:
            adj_char = input_matrix[row_idx + move[0]][col_idx + move[1]]
            if adj_char in ['#','$', '*', '+', '=', '-', '/', '&']:
                return True
        except IndexError:
            pass
    return False
 
def main():
    with open('Dec-3/input.txt') as f:
        lines = f.readlines()
    input_matrix = np.empty(shape=(len(lines),len(lines[0])), dtype=str)
    
    # Fill 2-D Matrix
    i = 0
    for line in lines:
        input_matrix[i] = list(line)
        i += 1
    
    sum = 0
    
    # Loop through each item and see if it has an adjacent symbol
    for i in range(0, len(input_matrix)):
        for j in range(0, len(input_matrix[i])):
            if adjacent_values(input_matrix, i, j) and input_matrix[i][j].isdigit():
                num = int(get_entire_num(input_matrix, i, j))
                sum += num
                
    print(sum)
if __name__ == "__main__":
    main()