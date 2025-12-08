# Puzzle solution for https://adventofcode.com/2025/day/6
#
# Each problem's numbers are arranged vertically; at the bottom of the problem
# is the symbol for the operation that needs to be performed. Problems are
# separated by a full column of only spaces. The left/right alignment of numbers
# within each problem can be ignored.
#
# Part 1: What is the grand total found by adding together all of the answers
# to the individual problems?


import argparse
import re

# Get the input filename from command line arguments

parser = argparse.ArgumentParser(
    prog="Advent Solver!", description="Find the Advent of Code solution for today."
)

parser.add_argument("filename", type=str, help="Input file with data.")

args = parser.parse_args()

print(f"Reading input from {args.filename}")

with open(args.filename, "r") as file:
    lines = file.readlines()

# Parse the data
print("Parsing the data...")
data_numbers = []
data_operands = []
for line in lines:
    if "*" in line:
        # This is the operands line, strings are fine
        data_operands.extend(line.split())
    else:
        # This is a line of numbers
        number_strings = line.split()
        number_ints = list(map(int, number_strings))
        data_numbers.append(number_ints)

# Process the problems
print("Processing problems...")
grand_total = 0
for i, operand in enumerate(data_operands):
    if operand == "*":
        solution = 1
        for nums in data_numbers:
            solution *= nums[i]
        grand_total += solution
    if operand == "+":
        solution = 0
        for nums in data_numbers:
            solution += nums[i]
        grand_total += solution
print(f"Grand total: {grand_total}")
