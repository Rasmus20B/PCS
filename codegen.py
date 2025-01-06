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
    stack = []

    def emit_intrinsic_call(self, e, intrinsic, code):
        for i in range(0, intrinsic.argn + 1):
            self.buffer = self.buffer[:self.buffer.rfind('\n')]
        self.buffer += f"\n{code}"
        args = e.child2
        while args:
            self.buffer += f" #{args.val}"
            args = args.child2
        self.buffer += "\n"
        pass

    def emit_function_call(self, e: pr.Binary):
        if type(e) is pr.Binary:
            self.buffer += f"call &{e.val}\n"

    def emit_unary_expr(self, e):
        if type(e) is pr.Unary and e.child is not None:
            if type(e.child) is pr.Unary:
                self.emit_unary_expr(e.child)
            elif type(e.child) is pr.Binary:
                self.emit_binary_expr(e.child)

        match e.ttype:
            case sc.TokenType.RETURN:
                self.buffer += "ret\n"

    def emit_binary_expr(self, e):
        if type(e) is pr.Binary and e.child2 is not None:
            self.emit_binary_expr(e.child2)

        elif type(e) is pr.Binary and e.child1 is not None:
            self.emit_binary_expr(e.child1)

        if type(e) is pr.Binary:
            match e.operand:
                case sc.TokenType.FUNC_CALL:
                    intrinsic = ins.intrins.get(e.val)
                    if intrinsic is not None:
                        self.emit_intrinsic_call(e, intrinsic, e.val)
                    else:
                        print("Found a function call")
                        self.emit_function_call(e)
                case sc.TokenType.EQ:
                    self.buffer += "seti $1\n"
                case sc.TokenType.ADD:
                    self.emit_binary_expr(e.child1)
                    self.buffer += "addi\n"
                case sc.TokenType.MUL:
                    self.buffer += "muli\n"
                case sc.TokenType.INT_LIT:
                    print(f"found arguments: {e.val}, {type(e)}")
                    self.buffer += f"pushi #{e.val}\n"
                    self.stack.append(e.val)
                case sc.TokenType.IDENT:
                    print(f"found args: {e.val}, {type(e)}")
                    # self.buffer += f"pushi {e.val}\n"

        if type(e) is pr.Unary:
            self.emit_unary_expr(e)
        print('here')

    def emit_compound(self, ch):
        for s in ch.children:
            if not s:
                break
            elif type(s) is pr.Unary:
                self.emit_unary_expr(s)
            elif type(s) is pr.Binary:
                self.emit_binary_expr(s)

    def emit_program(self):
        print("Code Emission==============")
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
