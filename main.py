#!/usr/bin/env python3

import argparse

import scanner
import parser
import codegen


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputFile", type=str)
    argparser.add_argument('-o', '--output')
    args = argparser.parse_args()

    with open(args.inputFile, "r") as f:
        content = scanner.progText(f.read())

    tokens = scanner.scan(content)
    parse = parser.parser(tokens)

    parse.parse_program()

    emitter = codegen.codegen(parse.ast)

    emitter.emit_program()

    if args.output:
        with open(args.output, "w") as f:
            for i in tokens:
                f.write(str(i.valType.value))


if __name__ == "__main__":
    main()
