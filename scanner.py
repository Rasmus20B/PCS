from enum import Enum

from attrs import define, field


@define
class progText():
    def nextTok(self):
        if self.index == len(self.text) - 1:
            return "EOF"
        self.index += 1
        return self.text[self.index]

    def curTok(self):
        if self.index == len(self.text) - 1:
            return "EOF"
        return self.text[self.index]

    text: str
    index: int = field(default=0)


class TokenType(Enum):
    VOID = 1
    INT = 2
    IDENT = 3
    OPEN_PAREN = 4
    CLOSE_PAREN = 5
    OPEN_BRACK = 6
    CLOSE_BRACK = 7
    SEMICOL = 8
    STR_LIT = 9
    INT_LIT = 10
    FLOAT_LIT = 11
    EOF = 12
    FLOAT = 13
    ADD = 14
    SUB = 15
    DIV = 16
    MUL = 17
    MOD = 18
    COMMA = 19
    LOG_AND = 20
    LOG_OR = 21
    BIT_AND = 22
    BIT_OR = 23
    EQ = 24
    NEQ = 25
    LE = 26
    GR = 27
    LEQ = 28
    GEQ = 29
    RETURN = 30
    ASYNC = 31
    FUNC_DECL = 32


class Token:
    def __init__(self, valType, val):
        self.valType = valType
        self.val = val

    valType: TokenType
    val: str


def scan(prog: progText):
    tokens = []
    cur = ""
    while True:
        cur = ""
        match prog.curTok():
            # Skipping whitespace
            case " " | "\n" | "\t":
                pass
            case "(":
                t = Token(valType=TokenType.OPEN_PAREN, val="")
                tokens.append(t)
            case ")":
                t = Token(valType=TokenType.CLOSE_PAREN, val="")
                tokens.append(t)
            case "{":
                t = Token(valType=TokenType.OPEN_BRACK, val="")
                tokens.append(t)
            case "}":
                t = Token(valType=TokenType.CLOSE_BRACK, val="")
                tokens.append(t)
            case ",":
                t = Token(valType=TokenType.COMMA, val="")
                tokens.append(t)
            case ";":
                t = Token(valType=TokenType.SEMICOL, val="")
                tokens.append(t)
            case "+":
                t = Token(valType=TokenType.ADD, val="+")
                tokens.append(t)
            case "-":
                t = Token(valType=TokenType.SUB, val="-")
                tokens.append(t)
            case "/":
                t = Token(valType=TokenType.DIV, val="/")
                tokens.append(t)
            case "*":
                t = Token(valType=TokenType.MUL, val="*")
                tokens.append(t)
            case "=":
                t = Token(valType=TokenType.EQ, val="=")
                tokens.append(t)
            case "&":
                if prog.nextTok() == "&":
                    t = Token(valType=TokenType.LOG_AND, val="&")
                    tokens.append(t)
                    continue
                else:
                    t = Token(valType=TokenType.BIT_AND, val="&&")
                    tokens.append(t)
                    continue
            case "%":
                t = Token(valType=TokenType.MOD, val="")
                tokens.append(t)
            case "EOF":
                t = Token(valType=TokenType.EOF, val="")
                tokens.append(t)
                break
            case _:
                if prog.curTok().isnumeric():
                    while prog.curTok().isnumeric():
                        cur += prog.curTok()
                        if prog.nextTok() in [" ", "\t", "\n", "(", ")", "{",
                                              "}", "EOF", "f", ";"]:
                            if prog.curTok() == "f":
                                t = Token(valType=TokenType.FLOAT_LIT, val=cur)
                            else:
                                t = Token(valType=TokenType.INT_LIT, val=cur)
                                tokens.append(t)
                                prog.index -= 1
                        break
                elif (prog.curTok().isalpha()):
                    while (prog.curTok().isalnum()):
                        cur += prog.curTok()
                        if prog.nextTok() in [" ", "\t", "\n", "(", ")",
                                              "{", "}", "EOF"]:
                            match cur:
                                case "int":
                                    t = Token(valType=TokenType.INT, val="int")
                                    tokens.append(t)
                                case "void":
                                    t = Token(valType=TokenType.VOID, val="void")
                                    tokens.append(t)
                                case "float":
                                    t = Token(valType=TokenType.FLOAT, val="float")
                                    tokens.append(t)
                                case "return":
                                    t = Token(valType=TokenType.RETURN, val="return")
                                    tokens.append(t)
                                case _:
                                    t = Token(valType=TokenType.IDENT, val=cur)
                                    tokens.append(t)
                                    prog.index -= 1
                            break
                elif (prog.curTok() == "\""):
                    prog.nextTok()
                    while (prog.curTok() not in ["\"", "EOF"]):
                        cur += prog.curTok()
                        prog.nextTok()
                    t = Token(valType=TokenType.STR_LIT, val=cur)
                    tokens.append(t)
                    prog.nextTok()
                    continue
        prog.nextTok()
        if (prog.curTok() == "EOF"):
            t = Token(valType=TokenType.EOF, val="")
            tokens.append(t)
            break
        else:
            continue
    return tokens
