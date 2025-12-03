# Puzzle solution for https://adventofcode.com/2025/day/2
# The ranges are separated by commas (,); each range gives its
# first ID and last ID separated by a dash (-).
#
# You can find the invalid IDs by looking for any ID
# which is made only of some sequence of digits repeated twice.
# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice)
# would all be invalid IDs.
#
# Your job is to find all of the invalid IDs that appear
# in the given ranges, and add them up. The sum is the Answer.


import argparse
import re


invalid_total = 0  # add up all of the invalid IDs

# Get the input filename from command line arguments

parser = argparse.ArgumentParser(
    prog="2025-12-02 parse IDs",
    description="Add up all of the invalid IDs in the ranges.",
)

parser.add_argument("filename", type=str, help="Input file containing the ID ranges.")

args = parser.parse_args()

print(f"Reading input from {args.filename}")

with open(args.filename, "r") as file:
    data = file.read()
    ranges = data.split(",")

for the_range in ranges:
    match = re.match(r"(\d+)-(\d+)", the_range)
    if match:
        start_id = int(match.group(1))
        end_id = int(match.group(2))
        print(f"Processing range: {start_id}-{end_id}")
        for id_num in range(start_id, end_id + 1):
            id_str = str(id_num)
            length = len(id_str)
            is_invalid = False
            # Check every number the length could be evenly divisible by
            for i in range(1, length // 2 + 1):
                # Check if evenly divisible
                if length % i == 0:
                    # Loop through all of the possible split points,
                    # to see if all segments are the same,
                    # always comparing against the first segment
                    start_split = i
                    while start_split + i <= length:
                        if id_str[:i] == id_str[start_split : start_split + i]:
                            is_invalid = True
                            start_split += i
                        else:
                            is_invalid = False
                            break
                    if is_invalid:
                        print(f">>> Invalid ID: {id_num}")
                        invalid_total += id_num
                        # We don't need to check any more, because at least one
                        # pattern detected
                        break
print(f"Total of all invalid IDs: {invalid_total}")
