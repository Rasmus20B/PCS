import types


class function:

    def __init__(self, ret: types.Type, argn: int, arg_types: {}, body: str):
        self.ret_type = ret
        self.argn = argn
        self.arg_types = arg_types
        self.assembly = body

    ret_type: type.Type
    argn: int
    arg_types = {}
    assembly: str = None
