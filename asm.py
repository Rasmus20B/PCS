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


def assemble(opcode, operands) -> []:
    code = []
    match opcode:
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
    return code


def tokenize(progtext):
    code = []
    i = 0
    operands = []
    while i < len(progtext):
        opcode = ""
        while i < len(progtext) and not progtext[i].isspace():
            opcode += progtext[i]
            i += 1
        while i < len(progtext) and progtext[i] != '\n':
            i += 1
            curop = ""
            while i < len(progtext) and not progtext[i].isspace():
                curop += progtext[i]
                i += 1
            operands.append(curop)
        for o in operands:
            print((o))
        print("done")
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
