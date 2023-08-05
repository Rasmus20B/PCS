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
        self.children = []
    children: []


class Decl_Statement(Node):
    def __init__(self, expr):
        self.child = expr
        pass

    child: Node


class Func_Decl(Node):
    def __init__(self, t, n, a):
        self.ftype = t
        self.name = n
        self.args = a
        self.child = ""

    ftype: str
    name: str
    args: []
    child: Compound


class lit_int(Node):
    def __init__(self, val):
        self.val = val
    val: int


class expr_statement(Node):
    def __init__(self, series):
        self.expr = []
    expr: []


class Unary(Node):
    child: Node


class Binary(Node):
    def __init__(self, op, c1, c2):
        self.operand = op
        self.child1 = c1
        self.child2 = c2

    operand: str
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

    def parse_expr(self, index):
        print(f"{self.tokens[index].valType}, {self.tokens[index].val}")
        index += 1
        match self.tokens[index].valType:
            case sc.TokenType.SEMICOL:
                return index, lit_int(self.tokens[index].val)
            case sc.TokenType.ADD:
                self.nextToken()
                o2 = self.peek()
                index += 3
                return index, Binary("Add", lit_int(self.tokens[index].val), lit_int(o2.val))
            case sc.TokenType.EOF:
                return index, None
            case _:
                print("Unrecognized expression")

    def parse_expr_statement(self, index):
        while self.tokens[index].valType is not sc.TokenType.SEMICOL:
            index, expr = self.parse_expr(index)

    def parse_statement(self, index):
        if self.tokens[index].valType == sc.TokenType.EOF:
            return index, None
        match self.tokens[index].valType:
            case sc.TokenType.SEMICOL:
                return index, None
            case sc.TokenType.EOF:
                return index, None
            case sc.TokenType.INT_LIT:
                index, expr = self.parse_expr(index)
                if expr is None:
                    return index, None
                return index, Decl_Statement(expr)
            case sc.TokenType.IDENT:
                index, expr = self.parse_expr(index)
                if expr is None:
                    return index, None
                return index, Decl_Statement(expr)
            case sc.TokenType.CLOSE_BRACK:
                return index, None
            case _:
                print("Unrecognized statement")
                return index, None
        return index, Decl_Statement()

    def parse_compound_statement(self, index):
        comp = Compound()
        while True:
            index, stat = self.parse_statement(index)
            if stat:
                comp.children.append(stat)
            else:
                break

        print(f"Statements in compound : {len(comp.children)}")
        # while self.tokens[index].valType is not sc.TokenType.CLOSE_BRACK:
        #     index += 1
        index += 1
        return index, comp

    def parse_func_Decl(self, index):
        # TODO: Implement specifiers and more types
        fun = Func_Decl("", "", "")
        match self.tokens[index].valType:
            case sc.TokenType.EOF:
                return index, fun
            case sc.TokenType.INT:
                fun.ftype = "int"
            case sc.TokenType.VOID:
                fun.ftype = "void"
            case sc.TokenType.FLOAT:
                fun.ftype = "int"
            case _:
                print(f"Unrecognized type specifier: \
                        {self.tokens[index].valType}")
                index += 1
                return index, fun
        index += 1

        match self.tokens[index].valType:
            case sc.TokenType.IDENT:
                fun.name = self.tokens[index].val
            case _:
                print("Expected Identifier for function")

        while self.tokens[index].valType \
                not in [sc.TokenType.SEMICOL,
                        sc.TokenType.OPEN_BRACK, sc.TokenType.EOF]:
            index += 1
        match self.tokens[index].valType:
            case sc.TokenType.SEMICOL:
                index += 1
                return index, fun
            case sc.TokenType.OPEN_BRACK:
                index += 1
                index, fun.child = self.parse_compound_statement(index)
                pass

        return index, fun

    def parse_root(self):
        while True:
            self.idx, func = self.parse_func_Decl(self.idx)
            if func.name != "":
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
            c: Compound = decl.child
            if (c):
                print("compound statement:")
                for com in c.children:
                    print(f"statement: {com.child}")
                    if type(com.child) == Binary:
                        print(f"{com.child.child1} \
                                {com.child.operand} \
                                {com.child.child2}")

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
