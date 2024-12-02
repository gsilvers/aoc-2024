#!/usr/bin/env python3

def parse_file(path_to_file: str) -> list[list[int]]:
    """ Given a file matching the pattern of day 2 of aoc returns a list of lists containing the data """

    file_list = []

    with open(path_to_file,"r") as infile:
            for line in infile:
                # Split the line into two parts
                row_as_list = [int(number) for number in line.split()]

                file_list.append(row_as_list)


    return file_list


def part_one(path_to_file: str) -> int:
    """ Performs Part 1 of Day 2 in Advent of Code 2024 """
    input_data = parse_file(path_to_file=path_to_file)

    report_status_codes = []

    for line_nr, report in enumerate(input_data):
        status = 1 # ok by default
        steps = []

        for index,item in enumerate(report[:-1]):
            steps.append(report[index+1] - item)

        all_less_than_2 = all(abs(x) <= 3  for x in steps) and all(abs(x) > 0 for x in steps)
        if not all_less_than_2:
            status = 0
        all_same_direction = all(x >= 0 for x in steps) or all(x <= 0 for x in steps)
        if not all_same_direction:
            status = 0

        report_status_codes.append(status)

    safe_reports = sum(report_status_codes)

    return safe_reports

def part_two(path_to_file: str) -> int:
    """ Performs part 2 of day 1 of advent of code 2024 """

    return 0

part_1_results = part_one(path_to_file = "20241202_input.txt")
print(f"part 1 result: {part_1_results}")



part_2_results = part_two(path_to_file = "20241202_input.txt")
print(f"part 2 result: {part_2_results}")