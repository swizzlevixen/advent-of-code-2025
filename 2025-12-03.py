# Puzzle solution for https://adventofcode.com/2025/day/3
#
# The batteries are arranged into banks; each line of digits in your input
# corresponds to a single bank of batteries. Within each bank, you need to
# turn on exactly two batteries; the joltage that the bank produces is equal to
# the number formed by the digits on the batteries you've turned on.
# For example, if you have a bank like 12345 and you turn on batteries 2 and 4,
# the bank would produce 24 jolts. (You cannot rearrange batteries.)
#
# You'll need to find the largest possible joltage each bank can produce.


import argparse

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

# Algorithm plan:
# - Look for the largest number in places 0 to length - 1
# - Keep the location of the largest number, ignore duplicates to the right
# - look for next largest number to the right of the first number
# - put them together and report the integer
# - sum all "joltages" and report the answer

total_joltage = 0  # Sum of joltage
batteries_allowed = 12  # Number of batteries that we are allowed to use

for line in lines:
    line = line.strip()
    jolt_val = []
    jolt_loc = []
    for batt in range(0, batteries_allowed):
        jolt_val.append(0)
        jolt_loc.append(0)
        if batt == 0:
            for i in range(0, len(line) - (batteries_allowed - 1)):
                if int(line[i]) > jolt_val[batt]:
                    jolt_val[batt] = int(line[i])
                    jolt_loc[batt] = i
        else:
            for i in range(
                jolt_loc[batt - 1] + 1, len(line) - (batteries_allowed - batt - 1)
            ):
                if int(line[i]) > jolt_val[batt]:
                    jolt_val[batt] = int(line[i])
                    jolt_loc[batt] = i
    batt_joltage = 0
    for value in jolt_val:
        batt_joltage *= 10
        batt_joltage += value
    print(f"Battery joltage for {line} is {batt_joltage}")
    total_joltage += batt_joltage

print(f"Total joltage: {total_joltage}")
