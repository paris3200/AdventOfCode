import sys
from Y2015.utils import read_lines


DATA = read_lines("data/07.data")
sys.setrecursionlimit(1000)


def check_numeric(input: str) -> int | str:
    """
    If a string is numeric, the int value is returned otherwise the string.

    Parameters
    ----------
        input:
            String to check if numeric

    Returns
    ----------
        Int value of input if it's numeric or the orignal string if it isn't.
    """
    if input.isnumeric():
        return int(input)
    else:
        return input


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
    if "AND" in instruction or "OR" in instruction:
        command["input1"] = check_numeric(instruction[0])
        command["gate"] = instruction[1]
        command["input2"] = check_numeric(instruction[2])
    elif "LSHIFT" in instruction or "RSHIFT" in instruction:
        command["input1"] = check_numeric(instruction[0])
        command["gate"] = instruction[1]
        command["shift-value"] = check_numeric(instruction[2])
    elif "NOT" in instruction:
        command["gate"] = instruction[0]
        command["input1"] = check_numeric(instruction[1])
    elif instruction[0].isnumeric():
        command["signal"] = int(instruction[0])
    else:
        command["input1"] = check_numeric(instruction[0])

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
    if wires is not None:
        for wire in wires:
            if wire["identifier"] == wire_id:
                return wire["signal"]


def check_if_signal_or_value(wires, input: str) -> None | int:
    """
    Checks if the signal is numeric or if it's a reference.  If reference,
    the signal value of the reference is returned if there is one.


    Parameters
    ----------
        wires:
            Current state of wires
        input:
            Input to be processed

    Returns:
        Signal Value at reference input or input value
    """
    if type(input) == int:
        return input
    else:
        if input.isnumeric():
            return int(input)
        else:
            return get_wire_signal(wires, input)


def process_instruction(instruction: dict, wires: list[dict[str, int]]) -> list[dict[str, int]] | None:
    signal_value = None
    if instruction["gate"] == "AND":
        wire1 = check_if_signal_or_value(wires, instruction["input1"])
        wire2 = check_if_signal_or_value(wires, instruction["input2"])

        if wire1 is not None and wire2 is not None:
            signal_value = wire1 & wire2
        else:
            return None
    elif instruction["gate"] == "OR":
        wire1 = check_if_signal_or_value(wires, instruction["input1"])
        wire2 = check_if_signal_or_value(wires, instruction["input2"])
        if wire1 is not None and wire2 is not None:
            signal_value = wire1 | wire2
        else:
            return None
    elif instruction["gate"] == "LSHIFT":
        wire1 = check_if_signal_or_value(wires, instruction["input1"])
        if wire1 is not None:
            signal_value = wire1 << instruction["shift-value"]
        else:
            return None
    elif instruction["gate"] == "RSHIFT":
        wire1 = check_if_signal_or_value(wires, instruction["input1"])
        if wire1 is not None:
            signal_value = wire1 >> instruction["shift-value"]
        else:
            return None
    elif instruction["gate"] == "NOT":
        wire1 = check_if_signal_or_value(wires, instruction["input1"])
        if wire1 is not None:
            # 16-bit unsigned Not
            signal_value = 65535 - wire1
        else:
            return None
    elif instruction["signal"] is not None:
        signal_value = instruction["signal"]
    else:
        wire1 = check_if_signal_or_value(wires, instruction["input1"])
        if wire1 is not None:
            signal_value = wire1
        else:
            return None

    # If wire exists already update it.
    for wire in wires:
        if wire["identifier"] == instruction["output"]:
            wire["signal"] = signal_value
            return wires
    wires.append({"identifier": instruction["output"], "signal": signal_value})
    return wires


def run_instructions(commands, wires):
    waitlist = []
    for command in commands:
        result_wires = process_instruction(command, wires)
        if result_wires is None:
            waitlist.append(command)
        else:
            wires = result_wires

    if waitlist != []:
        run_instructions(waitlist, wires)

    return wires


def part_one(data=DATA, wire=None):
    commands = []
    wires = []
    for instruction in data:
        commands.append(format_instruction(instruction))

    final_result = run_instructions(commands, wires)
    if wire:
        return get_wire_signal(final_result, wire)
    return wires


def part_two(data=DATA, wire=None):
    commands = []
    signal_override = part_one(wire="a")
    wires = []
    wires.append({"identifier": "b", "signal": signal_override})

    for instruction in data:
        # Prevent orignal signal from being applied
        if instruction != "19138 -> b":
            commands.append(format_instruction(instruction))

    final_result = run_instructions(commands, wires)
    if wire:
        return get_wire_signal(final_result, wire)
    return wires
