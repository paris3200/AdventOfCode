if __name__ != "__main__":
    from Y2015 import utils
    import hashlib
else:
    import utils
    import hashlib


def check_leading_zeros(input: str) -> bool:
    sub_str = input[:5]
    if sub_str == "00000":
        return True

    return False


def check_leading_zeros_two(input: str) -> bool:
    sub_str = input[:6]
    if sub_str == "000000":
        return True

    return False


def part_one(data="bgvyzdsv"):
    secret_key = data
    number = 11111
    result = secret_key + str(number)
    while check_leading_zeros(result) is False:
        number = int(number) + 1
        input = secret_key + str(number)
        input = input.encode()
        result = hashlib.md5(input)
        result = result.hexdigest()
    return number


def part_two(data="bgvyzdsv"):
    secret_key = data
    number = 111111
    result = secret_key + str(number)
    while check_leading_zeros_two(result) is False:
        number = int(number) + 1
        input = secret_key + str(number)
        input = input.encode()
        result = hashlib.md5(input)
        result = result.hexdigest()
    return number


if __name__ == "__main__":
    data = "../data/xx.data"
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
