def parse_lists(path_to_file: str) -> tuple[list[int], list:[int]]:
    """ given a path to a file with two ints seperated by spaces per line
    returns two lists one for each column """
    list1 = []
    list2 = []

    with open(path_to_file,"r") as infile:
            for line in infile:
                # Split the line into two parts
                parts = line.split()

                # Append the first number to list1 and the second number to list2
                list1.append(int(parts[0]))  # Convert to int or int as needed
                list2.append(int(parts[1]))

    return list1,list2
    

def part_one(path_to_file: str) -> int:
    """ Performs Part 1 of Day 1 in Advent of Code 2024 """
    list1, list2 = parse_lists(path_to_file = path_to_file)

    list1 = sorted(list1) 
    list2 = sorted(list2)

    distances = []

    for element_left, element_right in zip(list1,list2):
        distances.append(abs(element_right - element_left))

    result = 0
    result += sum(distances)
    return result

def part_two(path_to_file: str) -> int:
    """ Performs part 2 of day 1 of advent of code 2024 """
    list1, list2 = parse_lists(path_to_file = path_to_file)

    similarity_scores = []

    for element in list1:
        occurances = list2.count(element)
        score = occurances * element
        similarity_scores.append(score)

    result = 0
    result += sum(similarity_scores)

    return result

part_1_results = part_one(path_to_file = "/Users/gregsilverstein/Source/advent-of-code/20241201_input.txt")
print(f"part 1 result: {part_1_results}")



part_2_results = part_two(path_to_file = "/Users/gregsilverstein/Source/advent-of-code/20241201_input.txt")
print(f"part 2 result: {part_2_results}")

