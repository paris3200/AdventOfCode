from dataclasses import dataclass
import pprint


@dataclass
class Map:
    name: str
    mappings: list[dict[str, int]]


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    lines = []
    for line in data:
        if line != "\n":
            lines.append(line.rstrip().strip("\n"))
    return lines


def map_to_dict(destination_start: int, source_start: int, length: int) -> dict[str, int]:
    """
    Creates a dictionary with the keys being the source values and the values being the destinations values.

    Args:
        destination_start:  Destination range start
        source_start:       Source range start
        length:             Length of the range.

    Returns:
        Dict[source_start: int, source_end: int, dest_offset: int]
    """
    source_end = source_start+length
    destination_offset = destination_start - source_start

    return {"source_start": source_start, "source_end": source_end, "dest_offset": destination_offset}


def category_map(mappings: list[str]) -> list[dict[str, int]]:
    """
    Converts a list of strings in the format `[destination_start] [source_start] [range]` into a 
    list of dictionaries.

    Args:
        mappings: List of strings formatted as `[destination_start] [source_start] [range]`

    Returns:
        List[Dict[source_start: int, source_end: int, dest_offset: int]]
    """
    category_map = []
    for map in mappings:
        dest_start, source_start, range = map.split(" ")
        line_map = map_to_dict(int(dest_start), int(source_start), int(range))
        category_map.append(line_map)

    return category_map


def get_destination(map: list[dict[str, int]], source: int) -> int:
    destination = source
    for entry in map:
        if entry["source_start"] <= source <= entry["source_end"]:
            destination = source + entry["dest_offset"]
            return destination

    return destination


def generate_maps(lines: list[str]) -> list[map]:
    current_map = None
    maps = []
    mappings = []
    for line in lines:
        if ":" in line:
            if current_map:
                current_map.mappings = category_map(mappings)
                mappings = []

            label = line.strip().split(" ")[0]
            current_map = Map(name=label, mappings=[])
            maps.append(current_map)
        else:
            mappings.append(line)

    # Append the mappings for last category
    current_map.mappings = category_map(mappings)

    return maps


def part_one(filename: str):
    lines = read_lines(filename)
    seed_line = lines.pop(0).split(':')
    seeds = seed_line[1].strip().split(" ")
    seeds = list(map(int, seeds))
    maps = generate_maps(lines)

    # seed_to_soil = maps[0]
    # soil_to_fertilizer = maps[1]
    # fertilizer_to_water = maps[2]
    # water_to_light = maps[3]
    # light_to_temp = maps[4]
    # temp_to_humidity = maps[5]
    # humidity_to_location = maps[6]

    locations = []
    for seed in seeds:
        # print(f"Seed: {seed}")
        result = seed
        for map_table in maps:
            result = get_destination(map_table.mappings, result)
            # print(f"{map_table.name}: {result}\n")

        locations.append(result)

    return min(locations)


def part_two(filename: str):
    # lines = read_lines(filename)
    # seed_line = lines.pop(0).split(':')
    # seeds = seed_line[1].strip().split(" ")
    # seeds = list(map(int, seeds))
    # maps = generate_maps(lines)
    #
    # seeds = list(map(int, seeds))
    #
    # breakpoint()
    #
    #
    # locations = []
    # for seed in seeds:
    #     # print(f"Seed: {seed}")
    #     result = seed
    #     for map_table in maps:
    #         result = get_destination(map_table.mappings, result)
    #         # print(f"{map_table.name}: {result}\n")
    #
    #     locations.append(result)
    #
    # return min(locations)
    pass



if __name__ == "__main__":
    print("Part One")
    print(part_one("input"))

    print("Part Two")
    print(part_two("input"))
