import pytest

from Y2015.D07 import (
    format_instruction,
    process_instruction,
    part_one,
    part_two,
    get_wire_signal,
    Command,
)
from Y2015 import utils


def test_format_instruction_when_single_applied_to_wire():
    command = Command(output_signal=123, output_wire="x")
    assert command == format_instruction("123 -> x")


def test_format_instruction_when_wire_applied_to_wire():
    command = Command(wire1="lx", output_wire="a")
    assert command == format_instruction("lx -> a")


def test_format_instruction_and_gate():
    command = Command(wire1="x", wire2="y", gate="AND", output_wire="z")
    assert command == format_instruction("x AND y -> z")


def test_format_instruction_and_gate_signal_and_reference():
    command = Command(wire1_signal=1, gate="AND", wire2="io", output_wire="ip")
    assert command == format_instruction("1 AND io -> ip")


def test_format_instruction_or_gate():
    command = Command(wire1="x", gate="OR", wire2="y", output_wire="z")
    assert command == format_instruction("x OR y -> z")


def test_format_instruction_shift_gate():
    command = Command(wire1="p", gate="LSHIFT", shift_value=2, output_wire="q")
    assert command == format_instruction("p LSHIFT 2 -> q")


def test_format_instruction_not_gate():
    command = Command(gate="NOT", wire1="e", output_wire="f")
    assert command == format_instruction("NOT e -> f")


def test_get_wire_signal_returns_correct_value():
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    result = get_wire_signal(wires, "y")
    assert result == 456
    result = get_wire_signal(wires, "x")
    assert result == 123


def test_process_instruction_with_update_to_wire():
    command = format_instruction("x AND y -> x")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = []
    expected.append({"identifier": "x", "signal": 72})
    expected.append({"identifier": "y", "signal": 456})
    result = process_instruction(command, wires)
    assert result == expected
    pass


def test_process_instruction_and():
    command = format_instruction("x AND y -> d")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "d", "signal": 72})
    result = process_instruction(command, wires)
    assert result == expected


def test_process_instruction_and_missing_signal():
    """Gate should not return a signal if any inputs are missing a signal"""
    command = format_instruction("x AND y -> d")
    wires = []
    wires.append({"identifier": "y", "signal": 456})
    expected = None
    result = process_instruction(command, wires)
    assert result == expected


def test_process_instruction_or():
    command = format_instruction("x OR y -> e")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "e", "signal": 507})
    result = process_instruction(command, wires)
    assert result == expected


def test_process_instruction_rshift():
    command = Command(wire1="y", gate="RSHIFT", shift_value=2, output_wire="g")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "g", "signal": 114})
    result = process_instruction(command, wires)
    assert result == expected


def test_process_instruction_not():
    command = Command(wire1="y", gate="NOT", output_wire="i")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    expected = wires.copy()
    expected.append({"identifier": "i", "signal": 65079})
    result = process_instruction(command, wires)
    assert result == expected


def test_part_one_with_sample_data():
    instructions = utils.read_lines("data/07_test.data")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    wires.append({"identifier": "d", "signal": 72})
    wires.append({"identifier": "e", "signal": 507})
    wires.append({"identifier": "f", "signal": 492})
    wires.append({"identifier": "g", "signal": 114})
    wires.append({"identifier": "h", "signal": 65412})
    wires.append({"identifier": "i", "signal": 65079})
    result = part_one(instructions)
    assert result == wires


def test_part_one_with_sample_data_reordered():
    instructions = utils.read_lines("data/07_test_2.data")
    wires = []
    wires.append({"identifier": "x", "signal": 123})
    wires.append({"identifier": "y", "signal": 456})
    wires.append({"identifier": "d", "signal": 72})
    wires.append({"identifier": "e", "signal": 507})
    wires.append({"identifier": "f", "signal": 492})
    wires.append({"identifier": "g", "signal": 114})
    wires.append({"identifier": "h", "signal": 65412})
    wires.append({"identifier": "i", "signal": 65079})
    result = part_one(instructions, "x")
    assert result == 123


def test_case_problem_set_from_reddit_one():
    instructions = ["12 -> x", "1 OR x -> b", "b -> a"]
    result = part_one(instructions, "a")
    assert result == 13


def test_case_problem_set_from_reddit_two():
    instructions = ["0 -> b", "1 AND b -> a"]
    result = part_one(instructions, "a")
    assert result == 0


def test_part_one_correct_answer():
    result = part_one(wire="a")
    assert result == 16076


def test_part_two_correct_answer():
    result = part_two(wire="a")
    assert result == 2797
