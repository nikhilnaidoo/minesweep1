#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# count for empty spacs 
count = 0
# grid to work out
def minsweep(grid):
    grid = [["#","-","-","-","-"],
            ["#","-","-","-","-"],
            ["#","-","-","-","-"],
           ["#","-","-","-","-"],
           ["#","-","-","-","-"]]
    

# to find mines   
def convert(grid):
    # coordinates for each space finding # and adding 1 
    if mines == "#":
        if mines (x >=0 and x <= 3) and (y >= 0 and y <= 4)== "#":
            if mines [y][x+1] == "#": 
                grid[y][x+1] = +1
        if mines (x >=1 and x <= 4) and (y >= 0 and y <= 4)== "#":
            if mines[y][x-1] == "#": 
                grid[y][x-1] = +1 
        if mines (x >= 1 and x <= 4) and (y >= 1 and y <= 4)== "#":
            if mines[y-1][x-1] == "#":
                grid[y-1][x-1] = +1
        if mines (x >= 0 and x <= 3) and (y >= 1 and y <= 4) == "#":
            if mines [y-1][x+1] == "#":
                grid[y-1][x+1] = +1
        if mines (x >= 0 and x <= 4) and (y >= 1 and y <= 4)== "#":
            if mines [y-1][x] == "#":
                grid[y-1][x] = +1
        if mines(x >=0 and x <= 3) and (y >= 0 and y <= 3)=="#":
            if mines[y+1][x+1] == "#":  
                grid[y+1][x+1] = +1
        if mines (x >= 1 and x <= 4) and (y >= 0 and y <= 3)=="#":
            if mines[y+1][x-1] == "#":  
                grid[y+1][x-1] = +1 
        if mines (x >= 0 and x <= 4) and (y >= 0 and y <= 3)=="#":
            if mines[y+1][x] == "#": 
                grid[y+1][x] = +1 
        # return used to count each space in the grid        
        return convert(grid)
# converint the uncartered grid to minesweep. 
    minesweeper_grid =  convert(grid)               
# enabeling print               
for row in minesweeper_grid:
    print(" ".join(row))
    

