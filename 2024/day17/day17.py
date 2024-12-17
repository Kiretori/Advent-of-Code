from enum import Enum

with open("day17/input17.txt", "r") as f:
    adv_input = f.readlines()


class Register(Enum):
    A = 0
    B = 1
    C = 2

registers = {
    Register.A: 0,
    Register.B: 0,
    Register.C: 0,
}

A, B, C = Register.A, Register.B, Register.C

registers[A] = int(adv_input[0].split(":")[1].strip())
registers[B] = int(adv_input[1].split(":")[1].strip())
registers[C] = int(adv_input[2].split(":")[1].strip())
opcodes = [int(opcode) for opcode in adv_input[4].split(":")[1].strip().split(",")]


def combo(registers: dict[Register, int], operand: int) -> int:
    match operand:
        case 4:
            return registers[A]
        case 5:
            return registers[B]
        case 6:
            return registers[C]
        case _:
            return operand


def adv(registers: dict[Register, int], operand: int) -> None:
    registers[A] = registers[A] // 2**combo(registers, operand)


def bdv(registers: dict[Register, int], operand: int) -> None:
    registers[B] = registers[A] // 2**combo(registers, operand)


def cdv(registers: dict[Register, int], operand: int) -> None:
    registers[C] = registers[A] // 2**combo(registers, operand)


def bxl(registers: dict[Register, int], operand: int) -> None:
    registers[B] = registers[B] ^ operand


def bst(registers: dict[Register, int], operand: int) -> None:
    registers[B] = combo(registers, operand) % 8


def jnz(registers: dict[Register, int], operand: int, pc: int) -> int:
    if registers[A] != 0:
        return operand
    return pc


def bxc(registers: dict[Register, int]) -> None:
    registers[B] = registers[B] ^ registers[C]


def out(operand: int) -> int:
    return combo(registers, operand) % 8




def part1(registers):
    pc = 0

    output = []

    while pc < len(opcodes):
        match opcodes[pc]:
            case 0:
                adv(registers, opcodes[pc+1])
                pc += 2
            case 1:
                bxl(registers, opcodes[pc+1])
                pc += 2
            case 2:
                bst(registers, opcodes[pc+1])
                pc += 2
            case 3:
                pc = jnz(registers, opcodes[pc+1], pc)
            case 4:
                bxc(registers)
                pc += 2
            case 5:
                output.append(out(opcodes[pc+1]))
                pc += 2
                if registers[A] == 0:
                    break
            case 6:
                bdv(registers, opcodes[pc+1])
                pc += 2
            case 7:
                cdv(registers, opcodes[pc+1])
                pc += 2
            case _:
                print(f"Unknown opcode {pc}")
                break


    return(output)

print(part1(registers))


# PART 2

def part_2(registers) -> int:

    candidates = [0]
    for length in range(1, len(opcodes) + 1):
        out = []

        for num in candidates:
            for offset in range(2**3):
                a = (2**3) * num + offset
                registers[A] = a

                if part1(registers) == opcodes[-length:]:
                    out.append(a)

        candidates = out

    return min(candidates)

print(part_2(registers))