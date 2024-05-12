import func

intrins = {
        "nop": func.function(0, None, [], []),
        "delete": func.function(0, None, [], []),
        "return": func.function(0, None, {}, []),
        "call": func.function(1, None, {int}, ["location"]),
        "jmp": func.function(1, None, {int}, ["location"]),
        "jmpeq": func.function(0, None, {int}, ["location"]),
        "jmpneq": func.function(0, None, {int}, ["location"]),
        # "callAsync": func.function(0, None, {}),
        # "callAsyncID": func.function(0, None, {}),
        # "killAsync": func.function(0, None, {}),
        # "wait": func.function(0, None, {}),
        # "pushi": func.function(0, None, {}),
        # "seti": func.function(0, None, {}),
        # "pushf": func.function(0, None, {}),
        # "setf": func.function(0, None, {}),
        # "addi": func.function(0, None, {}),
        # "addf": func.function(0, None, {}),
        # "subi": func.function(0, None, {}),
        # "subf": func.function(0, None, {}),
        # "muli": func.function(0, None, {}),
        # "mulf": func.function(0, None, {}),
        # "divi": func.function(0, None, {}),
        # "divf": func.function(0, None, {}),

        "movePos": func.function(2, 2, [], []),
        "movePosTime": func.function(4, 4,
                                     [int, int, int, int],
                                     ["time", "mode", "x", "y"]),
        #
        # "enmCreate": func.function(0, None, {}),
        # "anmSetSprite": func.function(0, None, {}),
        #
        # "etNew": func.function(2, None, {}),
        # "etOn": func.function(1, None, {}),
        # "etSprite": func.function(0, None, {}),
        # "etOffset": func.function(0, None, {}),
        # "etAngle": func.function(0, None, {}),
        # "etSpeed": func.function(0, None, {}),
        # "etCount": func.function(0, None, {}),
        # "etAim": func.function(0, None, {}),

        "print": func.function(0, 0, [], [])
        }
