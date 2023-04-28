import random
import csv

def generate_maze(width, height, maze_number):
    maze = [[1] * width for _ in range(height)]

    num_wall_segments = maze_number // 5 + 1
    min_open_passage = max(1, 5 - maze_number // 10)  
    for _ in range(num_wall_segments):
        while True:
            x = random.randint(1, width - 3)
            y = random.randint(1, height - 3)
            length = random.randint(min_open_passage, width // 2) * 2
            if x % 2 == 0:
                x += 1
            if y % 2 == 0:
                y += 1

            if random.choice([True, False]):
                if x + length < width - 1:
                    for i in range(length):
                        maze[y][x + i] = 0
                    break
            else:
                if y + length < height - 1:
                    for i in range(length):
                        maze[y + i][x] = 0
                    break

    maze[0][1] = 1
    maze[height - 1][width - 2] = 1

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(["#" if cell == 0 else " " for cell in row]))

def save_maze_to_csv(maze, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(maze)

num_mazes = 50
maze_width = 11
maze_height = 11

for i in range(num_mazes):
    maze = generate_maze(maze_width, maze_height, i)
    print(f"Maze {i + 1}:")
    print_maze(maze)
    print()

    # Save the maze to a CSV file
    csv_filename = f"maze_{i + 1}.csv"
    save_maze_to_csv(maze, csv_filename)
