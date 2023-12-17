def solve_maze_with_move_limit(maze_file, max_moves):
    # Open and read files
    try:
        with open(maze_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{maze_file}' not found.")
        return

    # Extract only lines that belong to the maze
    maze_lines = [line.strip() for line in lines if line.strip()]

    # Start and end coordinates of the mazes
    start = None
    goal = None
    # Visited keeps track of visited positions
    visited = set()
    # Path stores the correct route to exit
    path = []

    # Finds the walls of the maze
    def get_wall_positions(row, col):
        walls = []

        # Up
        if row - 1 >= 0 and col < len(maze_lines[row - 1]):
            walls.append((row - 1, col))

        # Down
        if row + 1 < len(maze_lines) and col < len(maze_lines[row + 1]):
            walls.append((row + 1, col))

        # Left
        if col - 1 >= 0 and row < len(maze_lines) and col - 1 < len(maze_lines[row]):
            walls.append((row, col - 1))

        # Right
        if col + 1 < len(maze_lines[row]) and row < len(maze_lines):
            walls.append((row, col + 1))

        return walls

    def find_path(row, col, moves):
        # Check if path is valid with limits given
        if moves > max_moves:
            return False

        # If true > solution has been found
        if (row, col) == goal:
            return True

        visited.add((row, col))

        for walls in get_wall_positions(row, col):
            if walls not in visited:
                if find_path(walls[0], walls[1], moves + 1):
                    path.append((row, col))
                    return True

        return False

    # Get start and end coordinates dynamically
    start = None
    goal = None

    for i in range(len(maze_lines)):
        for j in range(len(maze_lines[i])):
            if maze_lines[i][j] == "^":
                start = (i, j)
                break  
        if start:
            break  

    if not start:
        print("Error: No starting point found in the maze.")
        return

    for i in range(len(maze_lines)):
        for j in range(len(maze_lines[i])):
            if maze_lines[i][j] == "E":
                goal = (i, j)
                break  
        if goal:
            break  

    if not goal:
        print("Error: No end point found in the maze.")
        return

    if find_path(start[0], start[1], 0):
        # Mark the correct path with + symbols
        for position in path:
            row, col = position
            maze_lines[row] = maze_lines[row][:col] + "+" + maze_lines[row][col + 1 :]

        # Save to .txt file
        output_file_name = f"maze_solution_{max_moves}_moves.txt"
        with open(output_file_name, "w") as output_file:
            for row in maze_lines:
                output_file.write(row + "\n")

        # Print messages
        print(f"Solution of the maze found with {max_moves} moves. Output saved to {output_file_name}")
        return

    print(f"Path not found within {max_moves} moves.")

while True:
    # Asking Name for maze
    maze_file = input("Enter the name of the maze text file (or type 'exit' to exit): ")

    if maze_file.lower() == 'exit':
        break

    # Max Moves
    max_moves_list = [20, 150, 200]
    for max_moves in max_moves_list:
        solve_maze_with_move_limit(maze_file, max_moves)