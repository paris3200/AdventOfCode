import utils


def is_valid(num):
    adjecent_digits = False
    num = list(num)
    for i in range(0, len(num) - 1):
        if int(num[i + 1]) < int(num[i]):
            return False
        if int(num[i + 1]) is int(num[i]):
            adjecent_digits = True

    return adjecent_digits


def possible_combinatations(floor, ceiling):
    # 273025, 767253
    solution = []
    for a in range(2, 8):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        for f in range(0, 10):
                            combo = int(
                                "".join(
                                    [str(a), str(b), str(c), str(d), str(e), str(f),]
                                )
                            )
                            if combo >= floor and combo <= ceiling:
                                if is_valid(str(combo)):
                                    solution.append(combo)
    return solution


def part_one():
    print(f"Part One")
    print(len(possible_combinatations(273025, 767253)))


def part_two():
    print(f"Part Two")


def test_if_it_works():
    assert is_valid("111111") == True
    assert is_valid("223450") == False
    assert is_valid("123789") == False


if __name__ == "__main__":

    part_one()
    part_two()
