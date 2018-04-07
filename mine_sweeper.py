# In the game of Minesweeper you are given a grid of size L x W
# that has a variable number of mines, M, in random locations within the grid.
# Write a function that generates random mine locations within the grid.

# 2
# How would you change your code if you also had to generate the tile numbers
# (the number on a non-mine tile should represent the number of mines in adjacent tiles)

# Your function gen(L, W, M), given L of 3, W of 3, M of 2 could return the following:
'''
+----+----+----+
| X  | 2  | 1  |
|    |    |    |
+--------------+
| 1  | 2  | X  |
|    |    |    |
+--------------+
| 0  | 1  | 1  |
|    |    |    |
+----+----+----+
'''

import random

# Method to create a 2D array (matrix) denoting the playing grid. All locations are initially set as "False"
# indicating absence of a mine. Indices for mines are chosen at random, and the locations are set to "True"
# in the grid

def initialize_matrix_and_add_mines(row, col, num_mines):
    # Define a 2-D array, with "False" which indicates no mine in that location
    mine_matrix = [[False for x in range(col)] for y in range(row)]

    while(num_mines > 0):
        rand_row = random.randint(0, row-1)
        rand_col = random.randint(0, col-1)
        #If mine is already present in the location, increment counter so that we 'repeat' the loop
        if(mine_matrix[rand_row][rand_col] == True):
            num_mines += 1
        else:
            # "True" indicates presence of mine
            mine_matrix[rand_row][rand_col] = True

        num_mines -= 1

    return(mine_matrix)


# For each location in the matrix, generate the list of 8 possible adjacent locations

def generate_adj_tile_list(mine_matrix, elem_row, elem_col):
    # Figuring out the dimensions of the matrix
    rows = len(mine_matrix)
    cols = len(mine_matrix[0])
    #print(rows, cols)
    adj_nodes_list = []

    # Find out the possible adjacent elements
    # 1. Add elements in the previous row, if possible
    if(elem_row - 1 >= 0):
        for j in range(elem_col-1, elem_col+2):
            if(j >= 0 and j < cols):
                adj_nodes_list.append([elem_row - 1, j])


    # 2. Add elements in the same row
    if(elem_col - 1 >= 0):
        adj_nodes_list.append([elem_row, elem_col - 1])
    if(elem_col + 1 < cols):
        adj_nodes_list.append([elem_row, elem_col + 1])


    # 3. Add elements in next row
    if (elem_row + 1 < rows):
        for j in range(elem_col - 1, elem_col + 2):
            if (j >= 0 and j < cols):
                adj_nodes_list.append([elem_row + 1, j])


    #print(adj_nodes_list)
    return(adj_nodes_list)


# Main

num_rows = 3
num_cols = 3
num_mines = 0

# Initialize mine matrix with mines at random locations
mine_matrix = initialize_matrix_and_add_mines(num_rows, num_cols, num_mines)
print(mine_matrix)

#Make a copy of the mine matrix for output
copy_matrix = list(map(list, mine_matrix))

# For every location in the matrix, calculate the number mines adjacent to each location
for i in range(num_rows):
    for j in range(num_cols):
        # Only check tiles that don't have mines
        if not (mine_matrix[i][j]):
            print(i,j, end=" ")
            # Generate adjacent tile lists
            adj_tiles_list = generate_adj_tile_list(mine_matrix, i, j)
            print(adj_tiles_list, end=" ")
            # Check all tiles in the adjacent tiles list and count the number of mines
            mine_count = 0
            for loc in adj_tiles_list:
               if(mine_matrix[loc[0]][loc[1]] == True):
                   mine_count = mine_count + 1
            print(mine_count)

            # Add count to copy_matrix
            copy_matrix[i][j] = mine_count

print("\n\n")
print(copy_matrix)