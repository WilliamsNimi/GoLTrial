"""WARNING: Unoptimized code, Presence of an infinite Loop.
    Abandon all hope all ye who shall enter here
"""
import numpy as np
import pandas as pd

ecoSystem = {(0,0): 0, (0,1): 1, (0,2): 1, (0,3): 0,(0,4): 0, (0,5): 0, (0,6): 1, (0,7): 0,
             (1,0): 1, (1,1): 0, (1,2): 1, (1,3): 0,(1,4): 1, (1,5): 0, (1,6): 0, (1,7): 0,
             (2,0): 0, (2,1): 0, (2,2): 0, (2,3): 0,(2,4): 0, (2,5): 0, (2,6): 0, (2,7): 0,
             (3,0): 0, (3,1): 0, (3,2): 0, (3,3): 1,(3,4): 0, (3,5): 0, (3,6): 1, (3,7): 1,
             (4,0): 0, (4,1): 0, (4,2): 1, (4,3): 1,(4,4): 0, (4,5): 0, (4,6): 1, (4,7): 0,
             (5,0): 0, (5,1): 0, (5,2): 0, (5,3): 0,(5,4): 0, (5,5): 0, (5,6): 0, (5,7): 1,
             (6,0): 0, (6,1): 0, (6,2): 1, (6,3): 1,(6,4): 0, (6,5): 0, (6,6): 1, (6,7): 0,
             (7,0): 0, (7,1): 0, (7,2): 1, (7,3): 0,(7,4): 0, (7,5): 0, (7,6): 0, (7,7): 0}

def generateNeighbours(cell):
    """Generate the neighbours associated with a cell"""
    list_neighs = []
    if cell[0] - 1 >= 0 and cell[0] - 1 <= 7:
        list_neighs.append((cell[0] - 1, cell[1]))
    if cell[1] - 1 >= 0 and cell[1] - 1 <= 7:
        list_neighs.append((cell[0], cell[1] - 1))
    if cell[1] + 1 >= 0 and cell[1] + 1 <= 7:
        list_neighs.append((cell[0], cell[1] + 1))
    if cell[0] + 1 >= 0 and cell[0] + 1 <= 7:
        list_neighs.append((cell[0] + 1, cell[1]))
    if (cell[0] - 1 >= 0 and cell[0] - 1 <= 7) and (cell[1] - 1 >= 0 and cell[1] - 1 <= 7):
        list_neighs.append((cell[0] - 1, cell[1] - 1))
    if (cell[0] + 1 >= 0 and cell[0] + 1 <= 7) and (cell[1] + 1 >= 0 and cell[1] + 1 <= 7):
        list_neighs.append((cell[0] + 1, cell[1] + 1))
    if (cell[0] + 1 >= 0 and cell[0] + 1 <= 7) and (cell[1] - 1 >= 0 and cell[1] - 1 <= 7):
        list_neighs.append((cell[0] + 1, cell[1] - 1))
    if (cell[0] - 1 >= 0 and cell[0] - 1 <= 7) and (cell[1] + 1 >= 0 and cell[1] + 1 <= 7):
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
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    count = 0
    for key, values in Board.items():
        board_list.append(values)
    for elements in board_list:
        if(count < 8):
            row1.append(elements)
            count+=1
        elif(count>=8 and count <16):
            row2.append(elements)
            count+=1
        elif(count>=16 and count <24):
            row3.append(elements)
            count+=1
        elif(count>=24 and count<32):
            row4.append(elements)
            count+=1
        elif(count>=32 and count <40):
            row5.append(elements)
            count+=1
        elif(count>=40 and count <48):
            row6.append(elements)
            count+=1
        elif(count>=48 and count<56):
            row7.append(elements)
            count+=1
        elif(count>=56 and count<64):
            row8.append(elements)
            count+=1
    
    board_array = np.array([row1, row2, row3, row4, row5, row6, row7, row8], dtype=object)
    
    df = pd.DataFrame(board_array)
    df.index = ["|","|","|","|","|","|","|","|"]
    df.columns = ["_","_","_","_","_","_","_","_"]
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
