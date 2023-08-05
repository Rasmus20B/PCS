#!/usr/bin/env python3

import argparse


class DWORD:
    def __init__(self, num):
        self.segments.append(int(num) & 0xFF000000 << 24)
        self.segments.append(int(num) & 0x00FF0000 << 16)
        self.segments.append(int(num) & 0x0000FF00 << 24)
        self.segments.append(int(num) & 0x000000FF)

    def clear(self):
        self.segments.clear()
    segments = []


labels = {}


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
        case "jmp":
            code.append(0x00)
            code.append(0x0C)
            addr = labels[operands[0]]
            par = DWORD(addr)
            for s in par.segments:
                code.append(s)
            par.clear()
        case "jmpeq":
            code.append(0x00)
            code.append(0x0D)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "jmpneq":
            code.append(0x00)
            code.append(0x0E)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "wait":
            code.append(0x00)
            code.append(0x17)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "pushi":
            code.append(0x00)
            code.append(0x2A)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "addi":
            code.append(0x00)
            code.append(0x32)

        case "enmCreate":
            code.append(0x01)
            code.append(0x2C)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()

        case "etNew":
            code.append(0x02)
            code.append(0x58)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()
        case "etOn":
            code.append(0x02)
            code.append(0x59)
            par = DWORD(operands[0])
            for s in par.segments:
                code.append(s)
            par.clear()

    return code


def tokenize(progtext):
    code = []
    i = 0
    operands = []
    while i < len(progtext):
        opcode = ""
        while i < len(progtext) and not progtext[i].isspace():
            if progtext[i] == ":":
                print(opcode)
                if (i == len(opcode)):
                    labels[str(opcode)] = i - len(opcode)
                else:
                    labels[str(opcode)] = i - (len(opcode) * 2) - 1
                i += 1
                continue
            opcode += progtext[i]
            i += 1
        while i < len(progtext) and progtext[i] != '\n':
            i += 1
            curop = ""
            while i < len(progtext) and not progtext[i].isspace():
                curop += progtext[i]
                i += 1
            operands.append(curop)
        code += assemble(opcode, operands)
        operands.clear()
        i += 1
    return code


def translate(progtext) -> []:
    code = tokenize(progtext)
    print(code)
    return code


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
