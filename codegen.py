import parser as pr
import scanner as sc


class codegen():
    def __init__(self, tree: pr.parser.ast):
        self.tree = tree
        self.buffer = ""

    tree: pr.parser.ast
    buffer: str

    def emit_unary_expr(self, e):
        if type(e) == pr.Unary and e.child is not None:
            if type(e.child) == pr.Unary:
                self.emit_unary_expr(e.child)
            if type(e.child) == pr.Binary:
                self.emit_binary_expr(e.child)

    def emit_binary_expr(self, e):
        if type(e) == pr.Binary and e.child2 is not None:
            self.emit_binary_expr(e.child2)
        if type(e) == pr.Binary and e.child1 is not None:
            self.emit_binary_expr(e.child1)
        if type(e) == pr.Binary:
            match e.operand:
                case sc.TokenType.EQ:
                    self.buffer += "seti 1\n"
                case sc.TokenType.ADD:
                    self.buffer += "addi\n"
                case sc.TokenType.INT_LIT:
                    self.buffer += f"pushi {e.val}\n"

        if type(e) == pr.Unary:
            self.emit_unary_expr(e)

    def emit_compound(self, cs):
        self.buffer += "start:\n"
        for s in cs.children:
            if not s:
                break
            elif type(s) == pr.Unary:
                self.emit_unary_expr(s)
            elif type(s) == pr.Binary:
                self.emit_binary_expr(s)

    def emit_program(self):
        for ci in self.tree.children:
            if type(ci) == pr.Unary:
                match ci.ttype:
                    case sc.TokenType.FUNC_DECL:
                        if not ci.child:
                            pass
                        else:
                            self.emit_compound(ci.child)
        print(self.buffer)
