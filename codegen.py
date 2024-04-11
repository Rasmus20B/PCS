import parser as pr
import scanner as sc
import intrins as ins


class codegen():
    def __init__(self, tree: pr.parser):
        self.tree = tree
        self.buffer = ""

    tree: pr.parser
    buffer = ""
    functions = {}
    variables = {}
    var_count = 0

    def emit_unary_expr(self, e):
        if type(e) is pr.Unary and e.child is not None:
            if type(e.child) is pr.Unary:
                self.emit_unary_expr(e.child)
            if type(e.child) is pr.Binary:
                self.emit_binary_expr(e.child)

        match e.ttype:
            case sc.TokenType.RETURN:
                self.buffer += "ret\n"

    def emit_binary_expr(self, e):
        if type(e) is pr.Binary and e.child2 is not None:
            self.emit_binary_expr(e.child2)

        if type(e) is pr.Binary and e.child1 is not None:
            self.emit_binary_expr(e.child1)

        if type(e) is pr.Binary:
            match e.operand:
                case sc.TokenType.FUNC_CALL:
                    self.buffer += f"call &{e.child1}\n"
                case sc.TokenType.EQ:
                    self.buffer += "seti $1\n"
                case sc.TokenType.ADD:
                    self.buffer += "addi\n"
                case sc.TokenType.MUL:
                    self.buffer += "muli\n"
                case sc.TokenType.INT_LIT:
                    self.buffer += f"pushi {e.val}\n"
        if type(e) is pr.Unary:
            self.emit_unary_expr(e)

    def emit_compound(self, ch):
        for s in ch.children:
            if not s:
                break
            elif type(s) is pr.Unary:
                self.emit_unary_expr(s)
            elif type(s) is pr.Binary:
                self.emit_binary_expr(s)

    def emit_program(self):
        for ci in self.tree.ast.children:
            if type(ci) is pr.Unary:
                match ci.ttype:
                    case sc.TokenType.FUNC_DECL:
                        print(f"Function: {ci.val} -> {ci.ttype} ")
                        if not ci.child:
                            continue
                        else:
                            self.buffer += f"{ci.val}:\n"
                            self.emit_compound(ci.child)
        print(self.buffer)
