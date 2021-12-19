from typing import List


def read_file_of_ints(filename) -> List[List[int]]:
    with open(filename, "r") as contents:
        lines = []
        for line in contents:
            data = line.strip()
            lines.append([int(a) for a in str(data)])

    return lines
