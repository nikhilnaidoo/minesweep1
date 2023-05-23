#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# inspration from https://exercism.org/

def convert_to_minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # start of new grid 
    minesweeper_grid = [["-"for _ in range(cols)] for _ in range(rows)]
    # for irerating over each cell in the gird to look for mines 
    for i in range (rows):
        for j in range(cols):
            # mark for mines in rows and columns
            if grid[i][j]=="#":
                minesweeper_grid[i][j] = "#"
             # else used to object    
            else:
                # to count the number of mines around a space useing nested loops
                count = 0 
                for count_1 in [-1,0,1]:
                    for count_2 in [-1, 0, 1]:
                        l = i + count_1
                        n = j + count_2
                        # to add 1 for each # found next to current cels
                        if 0<= l < rows and 0 <= n < cols and grid[l][n]== "#":
                            count +=1
                 # converting str count           
                minesweeper_grid[i][j] = str(count)
    # running the minesweeper_grid over grid           
    return minesweeper_grid
        
grid = [["-", "-", "#", "-", "-"],
        ["#", "-", "-", "-", "-"],
        ["#", "-", "-", "-", "-"],
        ["#", "-", "-", "-", "-"],
        ["#", "-", "-", "-", "-"]]
# running the minesweeper_grid over grid
minesweeper_grid = convert_to_minesweeper(grid)
# print converted minesweeper grid 
for row in minesweeper_grid:
    print(" ".join(row))
                            
                            

