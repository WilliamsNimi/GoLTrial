"""WARNING: Unoptimized code, Presence of an infinite Loop.
    Abandon all hope all ye who shall enter here
"""
import numpy as np
import pandas as pd

ecoSystem = {(0,0): 0, (0,1): 1, (0,2): 1, (0,3): 0,
             (1,0): 1, (1,1): 0, (1,2): 1, (1,3): 0,
             (2,0): 0, (2,1): 0, (2,2): 0, (2,3): 0,
             (3,0): 0, (3,1): 0, (3,2): 1, (3,3): 1}

def generateNeighbours(cell):
    """Generate the neighbours associated with a cell"""
    list_neighs = []
    if cell[0] - 1 >= 0 and cell[0] - 1 <= 3:
        list_neighs.append((cell[0] - 1, cell[1]))
    if cell[1] - 1 >= 0 and cell[1] - 1 <= 3:
        list_neighs.append((cell[0], cell[1] - 1))
    if cell[1] + 1 >= 0 and cell[1] + 1 <= 3:
        list_neighs.append((cell[0], cell[1] + 1))
    if cell[0] + 1 >= 0 and cell[0] + 1 <= 3:
        list_neighs.append((cell[0] + 1, cell[1]))
    if (cell[0] - 1 >= 0 and cell[0] - 1 <= 3) and (cell[1] - 1 >= 0 and cell[1] - 1 <= 3):
        list_neighs.append((cell[0] - 1, cell[1] - 1))
    if (cell[0] + 1 >= 0 and cell[0] + 1 <= 3) and (cell[1] + 1 >= 0 and cell[1] + 1 <= 3):
        list_neighs.append((cell[0] + 1, cell[1] + 1))
    if (cell[0] + 1 >= 0 and cell[0] + 1 <= 3) and (cell[1] - 1 >= 0 and cell[1] - 1 <= 3):
        list_neighs.append((cell[0] + 1, cell[1] - 1))
    if (cell[0] - 1 >= 0 and cell[0] - 1 <= 3) and (cell[1] + 1 >= 0 and cell[1] + 1 <= 3):
        list_neighs.append((cell[0] - 1, cell[1] + 1))
    return list_neighs

neighs = generateNeighbours((2,2))

def neighbough_iter(neighs):
    """ Iterate through the neigbours and aggregate their state"""
    neighbours_state = []
    count_1 = 0
    count_0 = 0
    for items in neighs:
        if ecoSystem[items] == 0:
            count_0 += 1
        else:
            count_1 += 1
    neighbours_state.append(count_1)
    neighbours_state.append(count_0)
    return neighbours_state

def render_board(Board):
    """ This function is supposed to render the board when called. 
    TO:DO find an optimal way to render this board """
    board_list = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    count = 0
    for key, values in Board.items():
        board_list.append(values)
    for elements in board_list:
        if(count < 4):
            row1.append(elements)
            count+=1
        elif(count>=4 and count <8):
            row2.append(elements)
            count+=1
        elif(count>=8 and count <12):
            row3.append(elements)
            count+=1
        elif(count>=12 and count<16):
            row4.append(elements)
            count+=1
    
    board_array = np.array([row1, row2, row3, row4], dtype=object)
    
    df = pd.DataFrame(board_array)
    df.index = ["|","|","|","|"]
    df.columns = ["_","_","_","_"]
    print(df)

render_board(ecoSystem)

pos_state_change = True
while(pos_state_change):
    cell_neighs = []
    neigh_state = []
    for cell, value in ecoSystem.items():
        if value == 1:
            cell_neighs = generateNeighbours(cell)
            neigh_state = neighbough_iter(cell_neighs)
            if neigh_state[0] < 2 or neigh_state[0] > 3:
                print("Alive: {}, Cell:{}".format(neigh_state, cell))
                ecoSystem[cell] = 0
                pos_state_change = True
            else:
                pos_state_change = False
        if value == 0:
            cell_neighs = generateNeighbours(cell)
            neigh_state = neighbough_iter(cell_neighs)
            if neigh_state[0] == 3:
                print("Dead: {}, Cell:{}".format(neigh_state, cell))
                ecoSystem[cell] = 1
                pos_state_change = True
            else:
                pos_state_change = False
    render_board(ecoSystem)
