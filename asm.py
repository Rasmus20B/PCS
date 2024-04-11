#!/usr/bin/env python3

import argparse
import struct


class DWORD:

    def __init__(self):
        return

    def set(self, num, flag: int):
        self.segments.append(int(num) & 0x000000FF)
        self.segments.append((int(num) & 0x0000FF00) >> 8)
        self.segments.append((int(num) & 0x00FF0000) >> 16)
        # VARIABLE: 1
        # ADDRESS: 2
        # CONSTANT: 0
        if flag == 1:
            self.segments.append((1))
        elif flag == 2:
            self.segments.append((2))
        else:
            self.segments.append((0))

    def __str__(self):
        i = 0
        i += (self.segments[0] & 0x000000FF)
        i += (self.segments[1] << 8) & 0x0000FF00
        i += (self.segments[2] << 16) & 0x00FF0000
        i += (self.segments[3] << 16) & 0xFF000000
        return str(i)

    def clear(self):
        self.segments.clear()
    segments = []


labels = {}

regs = {
    "r1": 0,
    "r2": 1,
    "r3": 2,
    "r4": 3,
    "r5": 4,
    "r6": 5,
    "r7": 6,
    "r8": 7,
    "r9": 8,
    "r10": 9,
    "r11": 10,
    "r12": 11,
    "r13": 12,
    "r14": 13,
    "r15": 14,
    "r16": 15
}


def encode_value(operand) -> DWORD:
    res = DWORD()
    if operand.startswith("$"):
        reg = operand.removeprefix("$")
        if reg in regs:
            idx = regs[reg]
            res.set(idx, 1)
    elif operand.startswith("&"):
        loc = operand.removeprefix("&")
        if loc in labels.keys():
            lab = labels[loc]
            res.set(lab, 2)
    elif operand.startswith("#"):
        res.set(operand.removeprefix("#"), 0)

    return res


def assemble(opcode, operands) -> []:
    code = []
    match opcode:
        case "nop":
            code.append(0x00)
            code.append(0x00)
        case "delete":
            code.append(0x00)
            code.append(0x01)
        case "ret":
            code.append(0x00)
            code.append(0x0A)
        case "call":
            code.append(0x00)
            code.append(0x0B)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "jmp":
            code.append(0x00)
            code.append(0x0C)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "jmpeq":
            code.append(0x00)
            code.append(0x0D)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "jmpneq":
            code.append(0x00)
            code.append(0x0E)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "callasync":
            code.append(0x00)
            code.append(0x0F)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "callasyncid":
            code.append(0x00)
            code.append(0x10)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "killasync":
            code.append(0x00)
            code.append(0x11)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "wait":
            code.append(0x00)
            code.append(0x17)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "pushi":
            code.append(0x00)
            code.append(0x2A)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "seti":
            code.append(0x00)
            code.append(0x2B)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "pushf":
            code.append(0x00)
            code.append(0x2C)
            par = struct.pack('<f', float(operands[0]))
            for s in par:
                code.append(s)
        case "pop":
            code.append(0x00)
            code.append(0x2E)
        case "addi":
            code.append(0x00)
            code.append(0x32)
        case "addf":
            code.append(0x00)
            code.append(0x33)
        case "subi":
            code.append(0x00)
            code.append(0x34)
        case "subf":
            code.append(0x00)
            code.append(0x35)
        case "muli":
            code.append(0x00)
            code.append(0x36)
        case "mulf":
            code.append(0x00)
            code.append(0x37)
        case "divi":
            code.append(0x00)
            code.append(0x38)
        case "divf":
            code.append(0x00)
            code.append(0x39)

        case "movePos":
            code.append(0x01)
            code.append(0x90)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "movePosTime":
            code.append(0x01)
            code.append(0x91)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[3])
            for s in par.segments:
                code.append(s)
            par.clear()

        case "enmCreate":
            code.append(0x01)
            code.append(0x2C)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[3])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[4])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[5])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "anmSetSprite":
            code.append(0x01)
            code.append(0x2f)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = DWORD(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()

        case "etNew":
            code.append(0x02)
            code.append(0x58)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etOn":
            code.append(0x02)
            code.append(0x59)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etSprite":
            code.append(0x02)
            code.append(0x5A)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = DWORD(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = DWORD(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etOffset":
            code.append(0x02)
            code.append(0x5B)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = DWORD(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = DWORD(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etAngle":
            code.append(0x02)
            code.append(0x5C)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etSpeed":
            code.append(0x02)
            code.append(0x5D)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etCount":
            code.append(0x02)
            code.append(0x5E)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[2])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etAim":
            code.append(0x02)
            code.append(0x5F)
            par = encode_value(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
            par = encode_value(operands[1])
            for s in par.segments:
                code.append(s)
            par.clear()

        case "print":
            code.append(0x03)
            code.append(0xE7)

        case _:
            print(f"Unknown Opcode: {opcode}")

    return code


def tokenize(progtext):
    code = []
    i = 0
    addr = 0
    lines = progtext.splitlines()

    for i, line in enumerate(lines):
        words = line.split(sep=" ")
        opcode = words[0]
        operands = words[1:]
        if opcode.endswith(":"):
            # label case
            if len(operands) > 0:
                print("Warning @{i}: operands to line starting with label will\
                      be ignored")
            label = opcode.removesuffix(":")
            if label in labels:
                print("Error @{i}: Label already defined")
                exit()
            labels[label] = addr + 8
        else:
            # regaular case
            code += assemble(opcode, operands)
            addr += 4 * len(operands) + 2

    return code


def genHeader():
    header = [0x7f, 0x44, 0x4d, 0x4c]
    ep = labels["start"]
    print("labels: ", labels)

    print(hex(ep))
    if ep:
        par = DWORD()
        par.set(ep, 2)
        for s in par.segments:
            header.append(s)
        par.clear()
    else:
        print("COULDN'T FIND START")

    print(header)
    return header


def translate(progtext) -> []:
    code = []
    code = tokenize(progtext)
    dml = genHeader() + code
    print(f"LENGTH: {len(dml)}")
    return dml


def gen_bytecode(code: str):
    return translate(code)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputFile", type=str)
    argparser.add_argument('-o', '--output')
    args = argparser.parse_args()

    with open(args.inputFile, "r") as f:
        content = f.read()

    out = translate(content)
    if args.output:
        with open(args.output, "wb") as f:
            f.write(bytes(out))
    else:
        with open("a.out", "wb") as f:
            f.write(bytes(out))

    return 0


if __name__ == "__main__":
    main()
