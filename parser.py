import scanner as sc
from typing import List


class Node:
    def __init__():
        pass


class Root(Node):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)
    children: []


class Compound(Node):
    def __init__(self):
        pass
    children: []


class Func_decl(Node):
    def __init__(self, t, n, a):
        self.ftype = t
        self.name = n
        self.args = a

    ftype: str
    name: str
    args: []
    child: Compound


class Unary(Node):
    child: Node


class Binary(Node):
    def __init__(self, c1, c2):
        self.child1 = c1
        self.child2 = c2

    child1: Node
    child2: Node


class Ternary(Node):
    def __init__(self, c1, c2, c3):
        self.child1 = c1
        self.child2 = c2
        self.child3 = c3

    child1: Node
    child2: Node
    child3: Node


class parser():
    symbols = []
    labels = []
    functions = []
    idx: int = 0
    tokens = List[sc.Token]
    buffer = str

    ast = []

    def __init__(self, tokens: List[sc.Token]):
        self.tokens = tokens

    def parse_compound_statement(self, index):
        print("FOUND A COMPOUND STATEMENT")
        while self.tokens[index].valType is not sc.TokenType.CLOSE_BRACK:
            index += 1
        index += 1
        return index, Compound()

    def parse_func_decl(self, index):
        # TODO: Implement specifiers
        spec = ""
        name = ""
        match self.tokens[index].valType:
            case sc.TokenType.EOF:
                return index, Func_decl(0, 0, 0)
            case sc.TokenType.INT:
                spec = "int"
            case sc.TokenType.VOID:
                spec = "void"
            case _:
                print(f"Unrecognized type specifier: \
                        {self.tokens[index].valType}")
                return index, Func_decl(0, 0, 0)

        index += 1

        match self.tokens[index].valType:
            case sc.TokenType.IDENT:
                name = self.tokens[index].val
            case _:
                print("Expected Identifier for function")

        while self.tokens[index].valType \
                not in [sc.TokenType.SEMICOL,
                        sc.TokenType.OPEN_BRACK, sc.TokenType.EOF]:
            index += 1

        return index, Func_decl(spec, name, "")

    def parse_root(self):
        while True:
            self.idx, func = self.parse_func_decl(self.idx)
            if func.name != 0:
                self.ast.append(func)
            match self.tokens[self.idx].valType:
                case sc.TokenType.SEMICOL:
                    self.idx += 1
                    continue
                case sc.TokenType.OPEN_BRACK:
                    self.idx += 1
                    self.idx, s = self.parse_compound_statement(self.idx)
                    func.child = s
                    continue
                case sc.TokenType.EOF:
                    break

        for decl in self.ast:
            print(f"Found func decl for: {decl.name} := {decl.ftype} ")

    def parse(self):
        a: sc.Token = self.peek()
        while a.valType is not sc.TokenType.EOF:
            match a:
                case sc.TokenType.VOID:
                    self.declaration()
                    continue
                case sc.TokenType.INT:
                    self.declaration()
                    continue
                case sc.TokenType.FLOAT:
                    self.declaration()
                    continue
                case sc.TokenType.IDENT:
                    self.ident()
                    continue
            a = self.nextToken()

    def ident(self):
        match self.nextToken():
            case sc.TokenType.OPEN_PAREN:
                self.function_call()
            case sc.TokenType.EQ:
                self.assignment()

    def assignment(self):
        pass

    def function_call(self):
        while self.nextToken().valType is not sc.TokenType.CLOSE_PAREN:
            pass

    def declaration(self):
        a = self.nextToken()
        match a:
            case sc.TokenType.IDENT:
                match self.nextToken().valType:
                    case sc.TokenType.OPEN_PAREN:
                        self.function_call()
                pass
            case _:
                print(f"Unexpected Token: {a.valType}")
                return 3

    def statement(self):
        pass

    def expression(self):
        pass

    def nextToken(self) -> sc.Token:
        if self.idx < len(self.tokens) - 1:
            self.idx += 1
        return self.tokens[self.idx]

    def peek(self) -> sc.Token:
        if self.idx < len(self.tokens):
            return self.tokens[self.idx + 1]
