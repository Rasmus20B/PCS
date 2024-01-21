import scanner as sc
import func as fn
from typing import List

precedence = {
        sc.TokenType.IDENT: -1,
        sc.TokenType.INT_LIT: -1,
        sc.TokenType.SEMICOL: -1,
        sc.TokenType.EQ: -1,
        sc.TokenType.ADD: 10,
        sc.TokenType.MUL: 11,
        sc.TokenType.SUB: 15,
        sc.TokenType.DIV: 20,
        }


class Node(object):
    def __init__():
        pass


class Unary(Node):
    def __init__(self, child, ttype, etype, val):
        self.ttype = ttype
        self.child = child
        self.etype = etype
        self.val = val
    child: Node
    ttype: sc.TokenType
    etype: str
    val: str


class Binary(Node):
    def __init__(self, op, val, c1, c2):
        self.operand = op
        self.val = val
        self.child1 = c1
        self.child2 = c2
    operand: str
    val: str
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


class Nary(Node):
    def __init__(self, ch):
        self.children = ch
    children = []
    ttype: sc.TokenType


class parser():
    symbols = []
    labels = []
    functions = {}
    idx: int = 0
    tokens = List[sc.Token]
    buffer = str
    ast = Nary
    stack: []

    def __init__(self, tokens: List[sc.Token]):
        self.tokens = tokens

    def print_unary_expr(self, e):
        print(f"op: {e.val}")
        if type(e) is Unary and e.child is not None:
            if type(e.child) is Unary:
                self.print_unary_expr(e.child)
            if type(e.child) is Binary:
                print("found BINARY inside unary")
                self.print_binary_expr(e.child)

    def print_binary_expr(self, e):
        if type(e) is Binary:
            print(f"op: {e.val}")
        if type(e) is Binary and e.child1 is not None:
            print("going left")
            self.print_binary_expr(e.child1)
        if type(e) is Binary and e.child2 is not None:
            print("going right")
            self.print_binary_expr(e.child2)
        if type(e) is Unary:
            self.print_unary_expr(e)

    def print_compound(self, ch):
        print("Compound Statement:")
        for s in ch.children:
            if not s:
                break
            elif type(s) is Unary:
                print("Found Unary Expr")
                self.print_unary_expr(s)
            elif type(s) is Binary:
                print("Found Binary Expr")
                self.print_binary_expr(s)

    def print_tree(self):
        for ci in self.ast.children:
            if type(ci) is Unary:
                print(ci)
                match ci.ttype:
                    case sc.TokenType.FUNC_DECL:
                        if not ci.child:
                            print(f"Found Function Declaration: \
                                  {ci.val} -> {ci.etype}")
                        else:
                            print(f"Found Function Definition: \
                                  {ci.val} -> {ci.etype}")
                            self.print_compound(ci.child)

    def parse_var_assignment(self):

        print("FOUND A VAR ASSIGNMENT")
        self.nextToken()
        lhs = self.parse_primary_expr()

        print(f"{lhs.val}")
        self.nextToken()
        return Binary(sc.TokenType.EQ,
                      "=",
                      lhs,
                      self.parse_binop_expr(0, self.parse_primary_expr())
                      )
    args = 0

    def parse_f_args(self):
        self.args += 1
        self.idx += 1
        t = self.tokens[self.idx]
        if t.valType == sc.TokenType.COMMA:
            self.idx += 1
            t = self.tokens[self.idx]
        if t.valType not in {sc.TokenType.CLOSE_PAREN,
                             sc.TokenType.COMMA}:
            ptype = t.valType
            return Unary(self.parse_f_args(), ptype, sc.TokenType.IDENT, t.val)
        else:
            self.idx += 1
            return

    def parse_identifier_u(self):
        if self.peek().valType == sc.TokenType.OPEN_PAREN:
            self.idx += 1
            return Binary(sc.TokenType.FUNC_CALL,
                          self.tokens[self.idx - 1].val,
                          self.tokens[self.idx - 1].val,
                          self.parse_f_args())
        else:
            num = Binary(sc.TokenType.IDENT,
                         self.tokens[self.idx].val,
                         None,
                         None)
            num.val = self.tokens[self.idx].val
            self.idx += 1
            return num

    def parse_int_literal_u(self):
        num = Binary(sc.TokenType.INT_LIT,
                     self.tokens[self.idx].val,
                     None,
                     None)
        num.val = self.tokens[self.idx].val
        self.idx += 1
        return num

    def parse_paren_expr_u(self):
        num = Binary(sc.TokenType.INT_LIT,
                     self.tokens[self.idx].val,
                     None,
                     None)
        num.val = self.tokens[self.idx].val
        self.idx += 1
        return num

    def parse_primary_expr(self):
        match self.tokens[self.idx].valType:
            case sc.TokenType.IDENT:
                return self.parse_identifier_u()
            case sc.TokenType.INT_LIT:
                return self.parse_int_literal_u()
            case sc.TokenType.OPEN_PAREN:
                return self.parse_paren_expr_u()
            case _:
                print("Error: Invalid Token for expression")
        pass

    def parse_ternary_expr(self):
        pass

    def parse_binop_expr(self, prec: int, lhs: Node) -> Binary:
        while True:
            t1 = self.tokens[self.idx].valType
            v1 = self.tokens[self.idx].val
            p1 = precedence[self.tokens[self.idx].valType]
            if p1 < prec:
                return lhs

            self.idx += 1

            rhs = self.parse_primary_expr()

            if not rhs:
                return None

            p2 = precedence[self.tokens[self.idx].valType]
            if p1 < p2:
                rhs = self.parse_binop_expr(p1 + 1, rhs)
                if not rhs:
                    return None
            lhs = Binary(t1, v1, rhs, lhs)

    def parse_expr(self):
        lhs = self.parse_primary_expr()
        if lhs is None:
            return None
        return self.parse_binop_expr(0, lhs)

    def parse_return_statement(self):
        self.idx += 1
        return Unary(self.parse_expr(),
                     sc.TokenType.RETURN,
                     sc.TokenType.RETURN,
                     "return")

    def parse_statement(self):
        a = self.nextToken()
        match a.valType:
            case sc.TokenType.OPEN_BRACK:
                return self.parse_compound_statement()
            case sc.TokenType.INT_LIT:
                return self.parse_expr()
            case sc.TokenType.INT:
                return self.parse_var_assignment()
            case sc.TokenType.IDENT:
                return self.parse_expr()
            case sc.TokenType.RETURN:
                return self.parse_return_statement()
            case sc.TokenType.CLOSE_BRACK:
                return
            case _:
                print("Error: Invalid statement")
                exit()

    def parse_compound_statement(self):

        # recall the cs constructor on each function call.
        # reference count from return will cause it to be
        # persistent between calls.
        cs = Nary([])
        while self.tokens[self.idx].valType != sc.TokenType.CLOSE_BRACK:
            cs.children.append(self.parse_statement())
        self.idx += 1
        return cs

    def parse_func_decl(self, ident: str, ftype: str):
        while self.tokens[self.idx].valType != sc.TokenType.CLOSE_PAREN:
            self.idx += 1
        self.idx += 1

        # add function symbol
        self.functions[ident] = fn.function(ftype, 0, {})
        match self.tokens[self.idx].valType:
            case sc.TokenType.OPEN_BRACK:
                return Unary(self.parse_compound_statement(),
                             sc.TokenType.FUNC_DECL,
                             ftype,
                             ident)
            case sc.TokenType.SEMICOL:
                return Unary(None,
                             sc.TokenType.FUNC_DECL,
                             ftype,
                             ident)
            case _:
                return None
        pass

    def parse_identifier(self, fname, ftype):
        a = self.nextToken()
        print(fname)
        match a.valType:
            case sc.TokenType.SEMICOL:
                return None
            case sc.TokenType.OPEN_PAREN:
                if fname and ftype:
                    return self.parse_func_decl(fname, ftype)
                elif fname:
                    pass
                else:
                    while self.tokens[self.idx] != sc.TokenType.CLOSE_PAREN:
                        self.idx += 1
            case sc.TokenType.EQ:
                return self.parse_var_assignment()
            case _:
                return None

    def parse_int(self):
        a = self.nextToken()
        match a.valType:
            case sc.TokenType.IDENT:
                return self.parse_identifier(a.val, "int")
            case _:
                print(f"Error: {a.val} is not an valid identifier")
                exit()

    def parse_program(self):
        while True:
            a: sc.Token = self.tokens[self.idx]
            fun = 0
            match a.valType:
                case sc.TokenType.EOF:
                    break
                case sc.TokenType.INT:
                    fun = self.parse_int()
                    self.ast.children.append(fun)
                case sc.TokenType.SEMICOL:
                    self.idx += 1
                case _:
                    print(f"Invalid token: {a.valType}")
                    exit()
        self.print_tree()

    def nextToken(self) -> sc.Token:
        if self.idx < len(self.tokens) - 1:
            self.idx += 1
        return self.tokens[self.idx]

    def peek(self) -> sc.Token:
        if self.idx < len(self.tokens):
            return self.tokens[self.idx + 1]
