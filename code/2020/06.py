import utils


def parse_forms(filename, part=1):
    lines = utils.read_lines(filename)
    forms = [[]]
    index = 0
    for line in lines:
        if line != "\n":
            forms[index].append(line)
        else:
            index += 1
            forms.append([])
    if part == 1:
        for index, form in enumerate(forms):
            # Convert to string
            string = "".join(map(str, form))

            # Remove duplicates
            string = "".join(set(string))

            # Sort
            forms[index] = "".join(sorted(string))

    elif part == 2:

        # Convert to sets
        for index, form in enumerate(forms):
            foo = []
            if len(form) > 1:
                for person in form:
                    foo.append(set(person))
            else:
                foo.append(set(form))
            forms[index] = foo

        # Find intersection of sets
        result = []
        for form in forms:
            if len(form) > 1:
                sets = set()
                for index, person in enumerate(form):
                    if index != 0:
                        sets = sets.intersection(person)
                    else:
                        sets.update(person)

                result.append(list(sets))
            else:
                result.append(list(form[0]))

        # Convert back to a string
        answer = ""
        for index, form in enumerate(result):
            for item in form:
                answer += item

        forms = answer

    return forms


def sum_counts(forms):
    count = 0
    for form in forms:
        count += len(form)

    return count


def part_one(input):
    print("Part One")
    result = parse_forms(input)
    sum = sum_counts(result)
    print(f"  Sum: {sum}")


def part_two(input):
    print("Part Two")
    result = parse_forms(input, part=2)
    sum = sum_counts(result)
    print(f"  Sum: {sum}")


def test_parse_forms():
    data = "data/06_tests.data"
    result = parse_forms(data)
    print(result)
    expected = ['abc', 'abc', 'abc', 'a', 'b']
    assert expected == result


def test_sum_counts():
    data = "data/06_tests.data"
    result = parse_forms(data)
    sum = sum_counts(result)
    assert 11 == sum


def test_parse_forms_part_two():
    data = "data/06_tests.data"
    result = parse_forms(data, part=2)
    expected = ['abcaab']
    assert expected == result


def test_parse_sums_part_two():
    data = "data/06_tests.data"
    result = parse_forms(data, part=2)
    sum = sum_counts(result)
    assert 6 == sum


if __name__ == "__main__":
    input = "data/06.data"
    part_one(input)
    part_two(input)
