import pcl_types


class function:
    def __init__(self,
                 ret: pcl_types.pcl_type,
                 argn: int,
                 arg_types: [],
                 arg_names: []
                 ):
        self.ret_type = ret
        self.argn = argn
        self.arg_types = arg_types
        self.arg_names = arg_names

    ret_type: pcl_types.pcl_type
    argn: int = 0
    arg_types = []
    arg_names = []
