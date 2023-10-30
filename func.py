import pcl_types


class function:
    def __init__(self, ret: pcl_types.pcl_type,
                 argn: int,
                 arg_types: {}):
        self.ret_type = ret
        self.argn = argn
        self.arg_types = arg_types

    ret_type: pcl_types.pcl_type
    argn: int
    arg_types = {}
    assembly: str = None
