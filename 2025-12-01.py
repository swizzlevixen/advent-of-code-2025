# Puzzle solution for https://adventofcode.com/2025/day/1

import argparse
import re


dial_position = 50  # Starting position of the safe dial
zero_count = 0  # Counter for how many times we've hit zero

# Get the input filename from command line arguments

parser = argparse.ArgumentParser(
    prog="2025-12-01 Decode", description="Find the door password."
)

parser.add_argument(
    "filename", type=str, help="Input file containing the safe rotations."
)

args = parser.parse_args()

print(f"Reading input from {args.filename}")

with open(args.filename, "r") as file:
    lines = file.readlines()

# Helper functions


def rotate_left(start, steps):
    global zero_count
    if steps > 100:
        zero_count += steps // 100
        steps = steps % 100
    result = start - steps
    if result < 0:
        result += 100
        if start != 0 and result != 0:
            print("<<Passed zero")
            zero_count += 1
    if result == 0:
        print("<<Result zero")
        zero_count += 1
    return result


def rotate_right(start, steps):
    global zero_count
    if steps > 100:
        zero_count += steps // 100
        steps = steps % 100
    result = start + steps
    if result > 99:
        result -= 100
        if start != 0 and result != 0:
            print("<<Passed zero")
            zero_count += 1
    if result == 0:
        print("<<Result zero")
        zero_count += 1
    return result


for line in lines:
    print(f"Processing line: {line.strip()}")
    match = re.match(r"[RL](\d+)", line.strip(), re.I)
    if match:
        direction = match.group(0)[0].upper()
        steps = int(match.group(1))
        print(f"Direction: {direction}, Steps: {steps}")
        if direction == "L":
            dial_position = rotate_left(dial_position, steps)
        elif direction == "R":
            dial_position = rotate_right(dial_position, steps)
        print(f"New position: {dial_position}")
    else:
        print(f"Invalid line format: {line.strip()}")

print(f"Total zero hits: {zero_count}")
