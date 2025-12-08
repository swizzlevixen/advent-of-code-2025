# Puzzle solution for https://adventofcode.com/2025/day/5
#
# The database operates on ingredient IDs. It consists of a list of fresh
# ingredient ID ranges, a blank line, and a list of available ingredient IDs.
#
# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs
# 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID
# is fresh if it is in any range.
#
# How many of the available ingredient IDs are fresh?


import argparse
import re

# Constants


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
print(f"Parsing the data...")
range_members = {}
ingredients = []
for line in lines:
    match_range = re.match(r"^(\d+)-(\d+)$", line)
    if match_range:
        start_id = int(match_range.group(1))
        end_id = int(match_range.group(2))
        range_members.update(list(range(start_id, end_id + 1)))
    match_ingredient = re.match(r"^(\d+)$", line)
    if match_ingredient:
        ingredients.append(int(match_ingredient.group(1)))
# print(range_members)
# print(ingredients)

# compare lists and return matches
# FIXME this runs out of memory in the full input data set
fresh_ingredients_count = len(set(range_members) & set(ingredients))
print(f"There are {fresh_ingredients_count} fresh ingredients")
