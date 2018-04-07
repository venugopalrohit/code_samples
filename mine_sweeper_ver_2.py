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

# This is a more efficient version  of the mine sweeper program that I implemented.
# The area/grid is represented as a matrix of the requested dimensions. Locations with mines are denoted by a "True"
# value and the non mine locations will have a number denoting the number of mines in their adjacent locations
# Step 1: Create a list of mine locations
# Step 2: Create an area/grid
# Step 3: For each mine location - set location in grid as "True" and increment adjacent location counters

import random

def create_mine_locations_list(num_rows, num_cols, num_mines):

    mine_list = []

    while (num_mines > 0):
        rand_row = random.randint(0, num_rows - 1)
        rand_col = random.randint(0, num_cols - 1)
        # If mine is already present in the location, increment counter so that we 'repeat' the loop
        if ((rand_row, rand_col) in mine_list):
            num_mines += 1
        else:
            # "True" indicates presence of mine
            mine_list.append((rand_row, rand_col))

        num_mines -= 1

    return (mine_list)


# For any location in the matrix, generate the list of 8 possible adjacent locations
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
                adj_nodes_list.append((elem_row - 1, j))


    # 2. Add elements in the same row
    if(elem_col - 1 >= 0):
        adj_nodes_list.append((elem_row, elem_col - 1))
    if(elem_col + 1 < cols):
        adj_nodes_list.append((elem_row, elem_col + 1))


    # 3. Add elements in next row
    if (elem_row + 1 < rows):
        for j in range(elem_col - 1, elem_col + 2):
            if (j >= 0 and j < cols):
                adj_nodes_list.append((elem_row + 1, j))


    #print(adj_nodes_list)
    return(adj_nodes_list)



# Seed the grid using the mine list
def seed_grid(game_grid, mine_list):
    # For each mine
    for mine_loc in mine_list:
        print(mine_loc[0], mine_loc[1], end=" : ")
        # Mark the location in the list as "True" indicating a mine
        game_grid[mine_loc[0]][mine_loc[1]] = True
        # Get the list of adjacent locations/tiles to the mine locations
        adj_tiles = generate_adj_tile_list(game_grid, mine_loc[0], mine_loc[1])
        print(adj_tiles)

        #For every adjacent tile that it not a mine, increment the value at that tile location
        for adj_tile_loc in adj_tiles:
            if not(adj_tile_loc in mine_list):
                game_grid[adj_tile_loc[0]][adj_tile_loc[1]] += 1


    print(game_grid)


# Main

# Minimum rows and columns is 2
# Number of mines >= 0

num_rows = 5
num_cols = 5
num_mines = 10

# Create mine_list (at random locations in grid)
mine_list = create_mine_locations_list(num_rows, num_cols, num_mines)
print(mine_list)
# Create game grid, with all locations initialized to 0 - indicating no mine adjacent to the tile
game_grid = [[0 for x in range(num_cols)] for y in range(num_rows)]
# Seed the grid with the mines in the correct locations and the indicate the number of mines adjacent to the remaining
# locations
seed_grid(game_grid, mine_list)