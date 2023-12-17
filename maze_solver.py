def solve_maze_with_move_limit(maze_file, max_moves):
    # Open and read files
    try:
        with open(maze_file, "r") as file:
            maze = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{maze_file}' not found.")
        return

    # Start and end coordinates of the mazes
    start = None
    goal = None
    # Visited keeps track of visited postions
    visited = set()
    # Path stores the correct route to exit
    path = []

    # Finds the walls of the mazes
    def get_wall_positions(row, col):
        walls = []

        # Up
        if row - 1 >= 0 and maze[row - 1][col] != "#":
            walls.append((row - 1, col))

        # Down
        if row + 1 < len(maze) and maze[row + 1][col] != "#":
            walls.append((row + 1, col))

        # Left
        if col - 1 >= 0 and maze[row][col - 1] != "#":
            walls.append((row, col - 1))

        # Right
        if col + 1 < len(maze[0]) and maze[row][col + 1] != "#":
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

    # Get start and end coordinates
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "^":
                start = (i, j)
            elif maze[i][j] == "E":
                goal = (i, j)

    if find_path(start[0], start[1], 0):
        # Mark the correct path with + symbols
        for position in path:
            row, col = position
            maze[row] = maze[row][:col] + "+" + maze[row][col + 1 :]

        # Save to .txt file
        output_file_name = f"maze_solution_{max_moves}_moves.txt"
        with open(output_file_name, "w") as output_file:
            for row in maze:
                output_file.write(row)

        # Print messages
        print(f"Solution of the maze found with {max_moves} moves. Output saved to {output_file_name}")
        return

    print(f"Path not found within {max_moves} moves.")


while True:
    # Prompt for maze file name
    maze_file = input("Enter the name of the maze text file (or type 'exit' to exit): ")

    if maze_file.lower() == 'exit':
        break

    # Specify max_moves_list based on requirements
    max_moves_list = [20, 150, 200]
    for max_moves in max_moves_list:
        solve_maze_with_move_limit(maze_file, max_moves)