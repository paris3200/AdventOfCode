from Y2015.utils import read_lines


DATA = read_lines("data/07.data")


def format_instruction(instruction: str) -> dict:
    command = {
        "input1": None,
        "input2": None,
        "gate": None,
        "shift-value": None,
        "signal": None,
        "output": None,
    }
    subcommand = instruction.split("->")

    # Assign output wire
    command["output"] = subcommand[1].strip()

    instruction = subcommand[0].split(" ")
    if instruction[0].isnumeric():
        command["signal"] = int(instruction[0])
    elif "AND" in instruction or "OR" in instruction:
        command["input1"] = instruction[0]
        command["gate"] = instruction[1]
        command["input2"] = instruction[2]
    elif "LSHIFT" in instruction or "RSHIFT" in instruction:
        command["input1"] = instruction[0]
        command["gate"] = instruction[1]
        command["shift-value"] = int(instruction[2])
    elif "NOT" in instruction:
        command["gate"] = instruction[0]
        command["input1"] = instruction[1]

    return command


def get_wire_signal(wires: list[dict[str, int]], wire_id: str) -> int | None:
    """
    Returns the signal value of the wire specified.

    Parameters
    ----------
        wires:
            Wires to be searched
        wire_id:
            Wire identifier whose signal is to be returned

    Returns:
        Signal Value of wire_id or None
    """
    for wire in wires:
        if wire["identifier"] == wire_id:
            return wire["signal"]


def process_instruction(instruction: dict, wires: list[dict[str, int]]) -> list:
    signal_value = None
    if instruction["gate"] == "AND":
        wire1 = get_wire_signal(wires, instruction["input1"])
        wire2 = get_wire_signal(wires, instruction["input2"])
        if wire1 and wire2:
            signal_value = wire1 & wire2
    elif instruction["gate"] == "OR":
        wire1 = get_wire_signal(wires, instruction["input1"])
        wire2 = get_wire_signal(wires, instruction["input2"])
        if wire1 and wire2:
            signal_value = wire1 | wire2
    elif instruction["gate"] == "LSHIFT":
        wire1 = get_wire_signal(wires, instruction["input1"])
        if wire1:
            signal_value = wire1 << instruction["shift-value"]
    elif instruction["gate"] == "RSHIFT":
        wire1 = get_wire_signal(wires, instruction["input1"])
        if wire1:
            signal_value = wire1 >> instruction["shift-value"]
    elif instruction["gate"] == "NOT":
        wire1 = get_wire_signal(wires, instruction["input1"])
        if wire1:
            # 16-bit unsigned Not
            signal_value = 65535 - wire1
    else:
        signal_value = instruction["signal"]

    # If wire exists already update it.
    for wire in wires:
        if wire["identifier"] == instruction["output"]:
            wire["signal"] = signal_value
            return wires

    # If no signal value, then there wasn't input on all of the gate inputs
    if signal_value:
        wires.append({"identifier": instruction["output"], "signal": signal_value})
    return wires


def part_one(data=DATA, wire=None):
    commands = []
    wires = []
    for instruction in data:
        commands.append(format_instruction(instruction))

    for command in commands:
        wires = process_instruction(command, wires)

    if wire:
        return get_wire_signal(wires, wire)
    return wires


def part_two(data):
    pass
