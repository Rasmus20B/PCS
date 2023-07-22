#!/usr/bin/env python3

import argparse

import scanner
import parser

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputFile", type=str)
    argparser.add_argument('-o', '--output')
    args = argparser.parse_args()

    with open(args.inputFile, "r") as f:
        content = scanner.progText(f.read())

    tokens = scanner.scan(content)
    parse = parser.parser()

    parse.parse()

    for t in tokens:
        print(f"{t.valType} : {t.val}\n ")

    if args.output:
        with open(args.output, "w") as f:
            for i in tokens:
                f.write(str(i.valType.value))
if __name__ == "__main__":
    main()
