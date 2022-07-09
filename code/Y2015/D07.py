from dataclasses import dataclass
from Y2015.utils import read_lines


DATA = read_lines("data/07.data")


@dataclass()
class Command:
    wire1: str = None
    wire1_signal: int = None
    wire2: str = None
    wire2_signal: int = None
    gate: str = None
    shift_wire: str = None
    shift_value: int = None
    output_signal: str = None
    output_wire: int = None


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


def format_instruction(instruction: str) -> Command():
    c = Command()
    subcommand = instruction.split("->")

    # Assign output wire
    if subcommand[1].strip().isnumeric():
        c.output_signal = int(subcommand[1])
    else:
        c.output_wire = subcommand[1].strip()

    command = subcommand[0].split(" ")
    if "AND" in command or "OR" in command:
        c.gate = command[1]

        if command[0].isnumeric():
            c.wire1_signal = int(command[0])
        else:
            c.wire1 = command[0]

        if command[2].isnumeric():
            c.wire2_signal = int(command[2])
        else:
            c.wire2 = command[2]

    elif "LSHIFT" in command or "RSHIFT" in command:
        c.gate = command[1]
        if command[0].isnumeric():
            c.wire1_signal = int(command[0])
        else:
            c.wire1 = command[0]

        if command[2].isnumeric():
            c.shift_value = int(command[2])
        else:
            c.shift_wire = command[2]
    elif "NOT" in command:
        c.gate = command[0]
        if command[1].isnumeric():
            c.wire1_signal = int(command[1])
        else:
            c.wire1 = command[1]
    elif command[0].isnumeric():
        c.output_signal = int(command[0])
    else:
        if command[0].isnumeric():
            c.wire1_signal = int(command[0])
        else:
            c.wire1 = command[0]

    return c


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


def process_instruction(
    instruction: Command(), wires: list[dict[str, int]]
) -> list[dict[str, int]] | None:
    signal_value = None
    c = instruction

    # Check if signal exists for wire references
    if c.wire1 is not None and c.wire1_signal is None:
        c.wire1_signal = get_wire_signal(wires, c.wire1)
    if c.wire2 is not None and c.wire2_signal is None:
        c.wire2_signal = get_wire_signal(wires, c.wire2)

    if c.gate == "AND":
        if c.wire1_signal is not None and c.wire2_signal is not None:
            signal_value = c.wire1_signal & c.wire2_signal
        else:
            return None

    elif c.gate == "OR":
        if c.wire1_signal is not None and c.wire2_signal is not None:
            signal_value = c.wire1_signal | c.wire2_signal
        else:
            return None
    elif c.gate == "LSHIFT":
        if c.wire1_signal is not None:
            signal_value = c.wire1_signal << c.shift_value
        else:
            return None
    elif c.gate == "RSHIFT":
        if c.wire1_signal is not None:
            signal_value = c.wire1_signal >> c.shift_value
        else:
            return None
    elif c.gate == "NOT":
        if c.wire1_signal is not None:
            # 16-bit unsigned Not
            signal_value = 65535 - c.wire1_signal
        else:
            return None
    elif c.output_signal is not None:
        signal_value = c.output_signal
    else:
        if c.wire1_signal is not None:
            signal_value = c.wire1_signal
        else:
            return None

    # If wire exists already update it.
    for wire in wires:
        if wire["identifier"] == c.output_wire:
            wire["signal"] = signal_value
            return wires
    wires.append({"identifier": c.output_wire, "signal": signal_value})
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
