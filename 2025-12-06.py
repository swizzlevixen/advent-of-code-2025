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
print(f"Part 1 Grand total: {grand_total}")

# ------
# Part 2
print("\nPart 2:\nParsing the data...")

# Uhhhh… matrix rotation, sort of...
# Inspired by this idea https://stackoverflow.com/a/8421412/429070
rotated = list(zip(*lines))[::-1]
data_numbers = []
data_operands = []
temp_nums = []
for column in rotated:
    the_str = "".join(column)
    if the_str.isspace():
        # This is the break between problems
        # Only problem is there isn't spaces after the last one,
        # so one more data append at the end
        if len(temp_nums) > 0:
            data_numbers.append(temp_nums)
        temp_nums = []
        continue
    if "+" in the_str:
        data_operands.append("+")
        the_str = the_str[:-1]
    if "*" in the_str:
        data_operands.append("*")
        the_str = the_str[:-1]
    num = int(the_str)
    temp_nums.append(num)
if len(temp_nums) > 0:
    data_numbers.append(temp_nums)  # to catch the last problem
# print(data_numbers)
# print(data_operands)

# Process the problems
print("Processing problems...")
assert len(data_numbers) == len(
    data_operands
), f"length of lists does not match:\nnumbers: {len(data_numbers)}, operands: {len(data_operands)}"
grand_total = 0
for i, operand in enumerate(data_operands):
    if operand == "*":
        solution = 1
        for num in data_numbers[i]:
            solution *= num
        print(f"* {data_numbers[i]} = {solution}")
    elif operand == "+":
        solution = 0
        for num in data_numbers[i]:
            solution += num
        print(f"+ {data_numbers[i]} = {solution}")
    else:
        print("Unknown operand")
        exit(1)
    grand_total += solution
print(f"Part 2 Grand total: {grand_total}")
# 15323929651338163 is too high
