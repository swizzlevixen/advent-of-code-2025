# Puzzle solution for https://adventofcode.com/2025/day/5
#
# The database operates on ingredient IDs. It consists of a list of fresh
# ingredient ID ranges, a blank line, and a list of available ingredient IDs.
#
# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs
# 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID
# is fresh if it is in any range.
#
# Part 1: How many of the available ingredient IDs are fresh?


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
print(f"Parsing the data...")
ranges = []
ingredients = []
for line in lines:
    match_range = re.match(r"^(\d+)-(\d+)$", line)
    if match_range:
        start_id = int(match_range.group(1))
        end_id = int(match_range.group(2))
        ranges.append(range(start_id, end_id + 1))
    match_ingredient = re.match(r"^(\d+)$", line)
    if match_ingredient:
        ingredients.append(int(match_ingredient.group(1)))

# compare ingredients and return matches
fresh_ingredients_count = 0
for ingredient in ingredients:
    for r in ranges:
        if ingredient in r:
            fresh_ingredients_count += 1
            break

print(f"There are {fresh_ingredients_count} fresh ingredients")

## Part 2
# How many ingredient IDs are considered to be fresh
# according to the fresh ingredient ID ranges?
# Remember that ranges overlap.

print("\nConsolidating ranges...")
ranges_count = 0  # Incorrect count so that the first `while` loop evaluates
while ranges_count != len(ranges):
    # While checks to see if the count of ranges has changed since last time
    #   through. If it has, that means we need to go through the list again
    ranges_count = len(ranges)
    # Compare the ranges
    for i in range(0, len(ranges)):
        overlap = False
        ranges_indices_to_delete = []
        # Putting this in a try because we may hit a bounds error
        #   because we're deleting list members while processing
        try:
            i_min = ranges[i][0]
            i_max = ranges[i][-1]
            for j in range(i + 1, len(ranges)):
                j_min = ranges[j][0]
                j_max = ranges[j][-1]
                if max(i_min, j_min) - min(i_max, j_max) <= 0:
                    # Then they overlap
                    # Method inspired via https://stackoverflow.com/a/39452639/429070
                    i_min = min(i_min, j_min)
                    i_max = max(i_max, j_max)
                    overlap = True
                    ranges_indices_to_delete.append(j)
        except IndexError:
            # we've reached the end of the list,
            # probably because we deleted the later indices
            break
        if overlap:
            ranges[i] = range(i_min, i_max + 1)
            # Delete them in reversed order, so the indices don't get offset
            for index in reversed(ranges_indices_to_delete):
                del ranges[index]

fresh_ids_count = 0
for r in ranges:
    fresh_ids_count += len(r)
print(f"Fresh ingredient IDs count: {fresh_ids_count}")
