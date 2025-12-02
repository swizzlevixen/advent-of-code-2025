# Puzzle solution for https://adventofcode.com/2025/day/1
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
            if length % 2 == 0:
                half = length // 2
                if id_str[:half] == id_str[half:]:
                    print(f">>> Invalid ID: {id_num}")
                    invalid_total += id_num
print(f"Total of all invalid IDs: {invalid_total}")
