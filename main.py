#!/usr/bin/env python3

import argparse

import scanner

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", type=str)
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    with open(args.inputFile, "r") as f:
        content = scanner.progText(f.read())

    print(content.text)
    tokens = scanner.scan(content)
    for t in tokens:
        val = t.val
        ty = t.valType
        print(f"{ty} : {val} \n")


if __name__ == "__main__":
    main()
