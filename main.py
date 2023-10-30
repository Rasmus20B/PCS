#!/usr/bin/env python3

import argparse

import scanner
import parser
import codegen
import asm


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputFile", type=str)
    argparser.add_argument('-o', '--output')
    args = argparser.parse_args()

    with open(args.inputFile, "r") as f:
        content = scanner.progText(f.read())

    tokens = scanner.scan(content)

    for t in tokens:
      print(t.valType)


    print("PARSING===================")
    parse = parser.parser(tokens)

    parse.parse_program()

    assembly = codegen.codegen(parse.ast)

    assembly.emit_program()

    output = asm.gen_bytecode(assembly.buffer)

    print(output)

    if args.output:
        with open(args.output, "wb") as f:
            f.write(bytes(output))


if __name__ == "__main__":
    main()
