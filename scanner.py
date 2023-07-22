from enum import Enum

class progText():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def nextTok(self):
        if self.index == len(self.text) - 1:
            return "EOF"
        self.index += 1
        return self.text[self.index]
    def curTok(self):
        if self.index == len(self.text) - 1:
            return "EOF"
        return self.text[self.index]

    text : str
    index : int

class TokenType(Enum):
    VOID = 1
    INT  = 2
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

class Token:
    def __init__(self, valType, val):
        self.valType = valType
        self.val = val

    valType : TokenType
    val : str


def scan(prog : progText):
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
            case ";":
                t = Token(valType=TokenType.SEMICOL, val="")
                tokens.append(t)
            case "EOF":
                t = Token(valType=TokenType.EOF, val="")
                tokens.append(t)
            case _:
                if prog.curTok().isnumeric():
                    while prog.curTok().isnumeric():
                        cur += prog.curTok()
                        if prog.nextTok() in [" ", "\t", "\n", "(", ")", "{", "}", "EOF", "f"]:
                            if prog.curTok() == "f":
                                t = Token(valType=TokenType.FLOAT_LIT, val=cur)
                            else:
                                t = Token(valType=TokenType.INT_LIT, val=cur)
                            tokens.append(t)
                            prog.index -= 1
                            break
                elif(prog.curTok().isalpha()):
                    while(prog.curTok().isalnum()):
                        cur += prog.curTok()
                        if prog.nextTok() in [" ", "\t", "\n", "(", ")", "{", "}", "EOF"]:
                            match cur:
                                case "int":
                                    t = Token(valType=TokenType.INT, val="")
                                    tokens.append(t)
                                case "void":
                                    t = Token(valType=TokenType.VOID, val="")
                                    tokens.append(t)
                                case "float":
                                    t = Token(valType=TokenType.FLOAT, val="")
                                    tokens.append(t)
                                case _:
                                    t = Token(valType=TokenType.IDENT, val=cur)
                                    tokens.append(t)
                                    prog.index -= 1
                            break
                elif(prog.curTok() == "\""):
                    prog.nextTok()
                    while(prog.curTok() not in ["\"", "EOF"]):
                        cur += prog.curTok()
                        prog.nextTok()
                    t = Token(valType=TokenType.STR_LIT, val=cur)
                    tokens.append(t)
        prog.nextTok()
        if(prog.curTok() == "EOF"):
            break
        else:
            continue
    return tokens
