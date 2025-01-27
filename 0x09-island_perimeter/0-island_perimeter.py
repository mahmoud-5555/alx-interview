""" This module is solution for Island Perimeter task. """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid. """
    result = 0
    for index_x, row in enumerate(grid):
        for index_y, element in enumerate(row):
            if element == 1:
                result += 4
        
                if index_x > 0:
                    if grid[index_x - 1][index_y] == 1:
                        result -= 1
        
                if index_x < len(grid) - 1:
                    if grid[index_x + 1][index_y] == 1:
                        result -= 1

                if index_y > 0:        
                    if row[index_y - 1] == 1:
                        result -= 1

                if index_y < len(row) - 1:        
                    if row[index_y + 1] == 1:
                        result -= 1
        
    return result


              
