import utils


def part_one(data):
    increase = 0
    for index in range(1,len(data)):
        if data[index-1] < data[index]:
            increase += 1

    return increase



def part_two(data):
    sums = []
    for index in range(0,len(data)):
        if index < len(data)-2:
            sums.append(data[index] + data[index+1] + data[index+2])
    return part_one(sums)


def test_part_one():
    data= [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = part_one(data)
    assert result == 7


def test_part_two():
    data= [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = part_two(data)
    assert result == 5


if __name__ == "__main__":
    data = utils.read_file("data/01.data", "list")
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
