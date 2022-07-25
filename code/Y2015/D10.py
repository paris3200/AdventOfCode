from itertools import groupby

if __name__ != "__main__":
    from Y2015 import utils
else:
    import utils


def create_segments(line: str) -> list[str]:
    if len(line) == 1:
        return [line]
    else:
        groups = [list(g) for k, g in groupby(line)]
        segments = []
        for g in groups:
            chars = ""
            for char in g:
                chars += char
            segments.append(chars)
    return segments


def look_say_segment(segment: str) -> str:
    count = len(segment)
    value = segment[0]
    return f"{count}{value}"


def look_say(input) -> str:
    segments = create_segments(input)
    output = ""
    for chunk in segments:
        output += look_say_segment(chunk)
    return output

def part_one(input: str, reps: int) -> tuple:
    phrase = input
    while(reps > 0):
        phrase = look_say(phrase)
        reps -= 1
    return len(phrase)



def part_two(data):
    pass


if __name__ == "__main__":
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
