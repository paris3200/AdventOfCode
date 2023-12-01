def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    for index, line in enumerate(data):
        if line != "\n":
            data[index] = line.rstrip().strip("\n")
    return data


def get_calibration_digits(input: str) -> int:
    chars = list(input)

    calibration_digits = []
    for char in chars:
        if char.isdigit():
            calibration_digits.append(char)

    return int(calibration_digits[0] + calibration_digits[-1])


def get_calibration_words(input: str) -> int:
    chars = list(input)
    number_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    calibration_digits = {}
    for index, char in enumerate(chars):
        if char.isdigit():
            calibration_digits[index] = char

    for word in number_words.keys():
        index = input.find(word)
        if index != -1:
            calibration_digits[index] = number_words[word]
        right_index = input.rfind(word)
        if right_index != -1 and right_index != index:
            calibration_digits[right_index] = number_words[word]

    keys = list(calibration_digits.keys())
    keys.sort()

    return int(str(calibration_digits[keys[0]]) + str(calibration_digits[keys[-1]]))


def part_one(filename: str) -> int:
    lines = read_lines(filename)
    calibration_sum = 0

    for line in lines:
        calibration_sum += get_calibration_digits(line)

    return calibration_sum


def part_two(filename: str) -> int:
    lines = read_lines(filename)
    calibration_sum = list()

    for line in lines:
        calibration_sum.append(get_calibration_words(line))

    return sum(calibration_sum)


if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
