def maze_solver(maze):
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    row, col = 0, 0
    direction = 0  # starting moving right
   
    path = [(row, col)]
    
    # Add a maximum step limit 
    max_steps = len(maze) * len(maze[0]) * 10  # Increased limit
    
    step_count = 0
    
    while step_count < max_steps:
        step_count += 1
        
        # Handle mirror interactions in CURRENT cell before moving
        cell_value = maze[row][col]
        
        if cell_value == 1:  # 45° mirror
            if direction == 0:  # right → up
                direction = 3
            elif direction == 1:  # down → left  
                direction = 2
            elif direction == 2:  # left → down
                direction = 1
            elif direction == 3:  # up → right
                direction = 0
                
        elif cell_value == -1:  # -45° mirror
            if direction == 0:  # right → down
                direction = 1
            elif direction == 1:  # down → right
                direction = 0
            elif direction == 2:  # left → up
                direction = 3
            elif direction == 3:  # up → left
                direction = 2
        
        #move to next cell based on updated direction
        row += directions[direction][0]
        col += directions[direction][1]
        
        #Check if we're out of bounds
        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
            break
            
        path.append((row, col))
    
    return path



maze = [[ 0, 0, 0, -1],

    [ 1, 0, 0, 1],

    [ 0, 0, 0, 0],

    [-1, 0, 0, 0]]


path = maze_solver(maze)
print(path)

