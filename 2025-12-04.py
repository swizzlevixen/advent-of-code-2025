# Puzzle solution for https://adventofcode.com/2025/day/4
#
# The rolls of paper (@) are arranged on a large grid; the input is the diagram
# The forklifts can only access a roll of paper if there are fewer than
# four rolls of paper in the eight adjacent positions.
# If you can figure out which rolls of paper the forklifts can access,
# they'll spend less time looking and more time breaking down the wall
# to the cafeteria.
#
# The example shows the accessible rolls marked with x in the diagram


import argparse

# Constants
SURROUND_LIMIT = 4

# Get the input filename from command line arguments

parser = argparse.ArgumentParser(
    prog="Advent Solver!", description="Find the Advent of Code solution for today."
)

parser.add_argument("filename", type=str, help="Input file with data.")

args = parser.parse_args()

print(f"Reading input from {args.filename}")

with open(args.filename, "r") as file:
    lines = file.readlines()

# Get rid of all the whitespace/CR before processing
striplines = []
for line in lines:
    line = line.rstrip()
    striplines.append(line)
lines = striplines

# Assumptions:
# The grid is completely rectangular
# The grid is made up of only `@` and `.` and later `x`

# Algorithm plan:
# check the grid of 8 spaces around each given roll `@` or `x`
# if there are <4 other rolls, replace this roll with an `x`
# Count as you go, or parse the diagram again and count each `x`
# Report the total number


def is_accessible(y, x):
    center_item = lines[y][x]
    surrounding_paper_count = 0
    # print(f"{center_item} {y},{x}")
    for grid_y in range(y - 1, y + 2):
        for grid_x in range(x - 1, x + 2):
            # test for negative bounds and not checking current y,x
            if grid_y >= 0 and grid_x >= 0:
                try:
                    # print(f"  ❔ {grid_y},{grid_x}: {lines[grid_y][grid_x]}")
                    grid_item = lines[grid_y][grid_x]
                    if grid_item in ("@x"):
                        if grid_y == y and grid_x == x:
                            # this is the center that we are searching around
                            pass
                        else:
                            # print(f"  {grid_item} at {grid_y},{grid_x}")
                            surrounding_paper_count += 1
                except IndexError:
                    # This should handle positive bounds errors
                    # print(f"  Index {grid_y},{grid_x} doesn't exist!")
                    pass
    if surrounding_paper_count < SURROUND_LIMIT:
        # print(f"  ✅ Surrounding paper count: {surrounding_paper_count}")
        return True
    else:
        # print(f"  ❌ Surrounding paper count: {surrounding_paper_count}")
        return False


def insert_character(str, char, at_index):
    return f"{str[:at_index]}{char}{str[at_index + 1:]}"


def print_grid(grid):
    print()
    for line in lines:
        print(line)
    print()


def clean_grid():
    global lines
    for i in range(0, len(lines)):
        lines[i] = lines[i].replace("x", ".")
    # print("Cleaned:")
    # print_grid(lines)


def process_grid():
    global lines
    global accessible_rolls
    # print_grid(lines)
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            # print(f"{y}, {x}")
            if lines[y][x] in ("@x"):
                if is_accessible(y, x):
                    lines[y] = insert_character(lines[y], "x", x)
                    accessible_rolls += 1
                    # print(f"  Updated: {lines[y]}")


# Process the grid
accessible_rolls = 0
last_accessible = -1  # Spiked value to make sure the first while passes
while accessible_rolls != last_accessible:
    last_accessible = accessible_rolls
    process_grid()
    clean_grid()

print(f"Accessible rolls: {accessible_rolls}")
# print_grid(lines)
