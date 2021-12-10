from typing import List


def read_file_of_ints(filename) -> List[int]:
    with open(filename, "r") as contents:
        int_list = []
        for line in contents:
            data = line.strip().split(",")
            for num in data:
                int_list.append(int(num))

    return int_list
