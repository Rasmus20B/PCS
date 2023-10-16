import func

intrins = {
        "nop": func(0, None, "nop"),
        "delete": func(0, None, "delete"),
        "return": func(0, None, "ret"),
        "call": func(0, None, "call"),
        "jmp": func(0, None, "jmp"),
        "jmpeq": func(0, None, "jmpeq"),
        "jmpneq": func(0, None, "jmpneq"),
        "callAsync": func(0, None, "callasync"),
        "callAsyncID": func(0, None, "callasyncid"),
        "killAsync": func(0, None, "killasync"),
        "wait": func(0, None, "wait"),
        "pushi": func(0, None, "pushi"),
        "seti": func(0, None, "seti"),
        "pushf": func(0, None, "pushf"),
        "setf": func(0, None, "setf"),
        "addi": func(0, None, "addi"),
        "addf": func(0, None, "addf"),
        "subi": func(0, None, "subi"),
        "subf": func(0, None, "subf"),
        "muli": func(0, None, "muli"),
        "mulf": func(0, None, "mulf"),
        "divi": func(0, None, "divi"),
        "divf": func(0, None, "divf"),

        "movePos": func(0, None, "movePos"),
        "movePosTime": func(0, None, "movePosTime"),

        "enmCreate": func(0, None, "enmcreate"),
        "anmSetSprite": func(0, None, "anmSetSprite"),

        "etNew": func(2, None, "etNew"),
        "etOn": func(1, None, "etOn"),
        "etSprite": func(0, None, "etSprite"),
        "etOffset": func(0, None, "etOffset"),
        "etAngle": func(0, None, "etAngle"),
        "etSpeed": func(0, None, "etSpeed"),
        "etCount": func(0, None, "etCount"),
        "etAim": func(0, None, "etAim"),
        }