def maze_solver(maze):
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Start at (0, 0) moving right
    row, col = 0, 0
    direction = 0  # start moving right
    
    path = [(row, col)]
    
    # First move from (0,0) - light is already in the maze at (0,0)
    # We need to process the starting cell if it has a mirror
    cell_value = maze[row][col]
    if cell_value == 1:  # 45° mirror at start
        direction = 1  # right → down
    elif cell_value == -1:  # -45° mirror at start
        direction = 3  # right → up
    
    while True:
        # Move to next cell
        row += directions[direction][0]
        col += directions[direction][1]
        
        # Check if out of bounds
        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
            break
            
        path.append((row, col))
        
        # Process mirror in the current cell
        cell_value = maze[row][col]
        
        if cell_value == 1:  # 45° mirror
            if direction == 0: direction = 1    # right → down
            elif direction == 1: direction = 0  # down → right
            elif direction == 2: direction = 3  # left → up  
            elif direction == 3: direction = 2  # up → left
                
        elif cell_value == -1:  # -45° mirror
            if direction == 0: direction = 3    # right → up
            elif direction == 1: direction = 2  # down → left
            elif direction == 2: direction = 1  # left → down
            elif direction == 3: direction = 0  # up → right
    
    return pat