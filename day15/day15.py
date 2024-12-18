"""
--- Day 15: Warehouse Woes ---

You appear back inside your own mini submarine! Each Historian drives their mini submarine in a different direction; maybe the Chief has his own submarine down here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer inspection, they seem quite anxious, so you drive your mini submarine over to see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that food needs to be stored somewhere. That's why these lanternfish have built elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot that operates one of their most important warehouses! It is currently running amok, pushing around boxes in the warehouse with no regard for lanternfish logistics or lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an unpredictable robot so they could shut it off. However, if you could anticipate the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the robot will attempt to make (your puzzle input). The problem is that the movements will sometimes fail as boxes are shifted around, making the actual movements of the robot difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^

As the robot (@) attempts to move, if there are any boxes (O) in the way, the robot will also attempt to push those boxes. However, if this action would cause the robot or a box to move into a wall (#), nothing moves instead, including the robot. The initial positions of these are shown on the map at the top of the document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, > for right) that the robot will attempt to make, in order. (The moves form a single giant sequence; they are broken into multiple lines just to make copy-pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<

Were the robot to attempt the given sequence of moves, it would push around the boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

The larger example has many more moves; after the robot has finished those moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########

The lanternfish use their own custom Goods Positioning System (GPS for short) to track the locations of the boxes. The GPS coordinate of a box is equal to 100 times its distance from the top edge of the map plus its distance from the left edge of the map. (This process does not stop at wall tiles; measure all the way to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 4 = 104.

#######
#...O..
#......

The lanternfish would like to know the sum of all boxes' GPS coordinates after the robot finishes moving. In the larger example, the sum of all boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is finished moving, what is the sum of all boxes' GPS coordinates?
"""

def load_data(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        split = lines.index('')
        warehouse = lines[:split]
        moves = lines[split+1:]
        moves_one_line = ''.join(moves)
    return [list(row) for row in warehouse], moves_one_line

def try_move(m, warehouse, rows, cols):
    i_robot = 0
    j_robot = 0
    for i in range(rows):
        for j in range(cols):
            if warehouse[i][j] == '@':
                i_robot = i
                j_robot = j
                break
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Map to > < v ^
    if m == '^':
        direction = directions[3]
    elif m == 'v':
        direction = directions[2]
    elif m == '<':
        direction = directions[1]
    elif m == '>':
        direction = directions[0]
        
    i_new = i_robot + direction[0]
    j_new = j_robot + direction[1]
    
    if warehouse[i_new][j_new] == '#': # If we hit a wall do nothing
        return
    if warehouse[i_new][j_new] == '.': # If we hit an empty space move the robot
        warehouse[i_new][j_new] = '@'
        warehouse[i_robot][j_robot] = '.'
        return
    
    if warehouse[i_new][j_new] in ['O', '[', ']'] : # If we hit a box
        i_empty = None
        j_empty = None
        while warehouse[i_new][j_new] != '#': # We try to find an empty space to shift all boxes in the middle
            i_new += direction[0]
            j_new += direction[1]
            if warehouse[i_new][j_new] == '.':
                i_empty = i_new
                j_empty = j_new
                break
        if i_empty is not None and j_empty is not None: # If we actually found an empty space
            
            i = i_empty
            j = j_empty
            for k in range(abs((i_robot - i_empty) + (j_robot - j_empty))): # Need to shift k times
                warehouse[i][j] = warehouse[i -direction[0]][j - direction[1]]
                i = i - direction[0]
                j = j - direction[1]
            warehouse[i_robot][j_robot] = '.'
            return                            
    

def puzzle1(file):
    warehouse, moves = load_data(file)
    rows = len(warehouse)
    cols = len(warehouse[0])
    
    for m in moves:
        try_move(m, warehouse, rows, cols)
        
    for i in range(rows):
        print(''.join(warehouse[i]))
    
    gps = 0
    for i in range(rows):
        for j in range(cols):
            if warehouse[i][j] == 'O':
                gps += 100 * i + j
                
    print(f"part1: {gps}")
    
puzzle1('input.txt')

"""
--- Part Two ---

The lanternfish use your information to find a safe moment to swim in and turn off the malfunctioning robot! Just as they start preparing a festival in your honor, reports start coming in that a second warehouse's robot is also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. There is one key difference: everything except the robot is twice as wide! The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for each tile, make the following changes:

    If the tile is #, the new map contains ## instead.
    If the tile is O, the new map contains [] instead.
    If the tile is ., the new map contains .. instead.
    If the tile is @, the new map contains @. instead.

This will produce a new warehouse map which is twice as wide and with wide boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################

Because boxes are now twice as wide but the robot is still the same size and speed, boxes can be aligned such that they directly push two other boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^

After appropriately resizing this map, the robot would push around these boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############

This warehouse also uses GPS to locate the boxes. For these larger boxes, distances are measured from the edge of the map to the closest edge of the box in question. So, the box shown below has a distance of 1 from the top edge of the map and 5 from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........

In the scaled-up version of the larger example from above, after the robot has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################

The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. What is the sum of all boxes' final GPS coordinates?

"""

def try_move2(m, warehouse, rows, cols):
    i_robot, j_robot = -1, -1
    for i in range(rows):
        for j in range(cols): 
            if warehouse[i][j] == '@':
                i_robot, j_robot = i, j
                break
        if i_robot != -1:
            break
    
    directions = {
        '^': (-1, 0),  
        'v': (1, 0),   
        '<': (0, -1),  
        '>': (0, 1)    
    }
    direction = directions[m]
    i_new, j_new = i_robot + direction[0], j_robot + direction[1]
    
    
    if warehouse[i_new][j_new] == '.':
        warehouse[i_new][j_new] = '@'
        warehouse[i_robot][j_robot] = '.'
        return
    
    if (0 <= i_new < rows and 0 <= j_new + 1 < cols and
        warehouse[i_new][j_new] == '[' and warehouse[i_new][j_new + 1] == ']'):
        
        i_box_next, j_box_next = i_new + direction[0], j_new + direction[1]
        
        if m == '^' or m == 'v': 
            if (0 <= i_box_next < rows and 
                warehouse[i_box_next][j_new] == '.' and warehouse[i_box_next][j_new + 1] == '.'):
                
                warehouse[i_box_next][j_new] = '['
                warehouse[i_box_next][j_new + 1] = ']'
                warehouse[i_new][j_new] = '@'
                warehouse[i_new][j_new + 1] = '.'
                warehouse[i_robot][j_robot] = '.'
                warehouse[i_robot][j_robot + 1] = '.'
        
        elif m == '<' or m == '>':  
            if (0 <= j_box_next < cols and 0 <= j_box_next + 1 < cols and
                warehouse[i_new][j_box_next] == '.' and warehouse[i_new][j_box_next + 1] == '.'):
                
                warehouse[i_new][j_box_next] = '['
                warehouse[i_new][j_box_next + 1] = ']'
                warehouse[i_new][j_new] = '@'
                warehouse[i_new][j_new + 1] = '.'
                warehouse[i_robot][j_robot] = '.'
                warehouse[i_robot][j_robot + 1] = '.'


def puzzle2(file):
    warehouse, moves = load_data(file)
    rows = len(warehouse)
    cols = len(warehouse[0])
    new_warehouse = []
    for i in range(rows):
        new_warehouse.append([])
        for j in range(cols):
            if warehouse[i][j] == '#':
                new_warehouse[i].append('#')
                new_warehouse[i].append('#')

            elif warehouse[i][j] == 'O':
                new_warehouse[i].append('[')
                new_warehouse[i].append(']')
            elif warehouse[i][j] == '.':
                new_warehouse[i].append('.')
                new_warehouse[i].append('.')
            elif warehouse[i][j] == '@':
                new_warehouse[i].append('@')
                new_warehouse[i].append('.')
    
    
    for i in range(rows):
        print(''.join(new_warehouse[i]))
        
    for m in moves:
        try_move2(m, new_warehouse, rows, cols)
        
    for i in range(rows):
        print(''.join(new_warehouse[i]))
    
    gps = 0
    for i in range(rows):
        for j in range(cols):
            if new_warehouse[i][j] == '[':
                gps += 100 * i + j
                
    print(f"part2: {gps}")
        
puzzle2('example.txt')