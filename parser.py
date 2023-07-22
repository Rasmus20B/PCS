import scanner

class parser():
    symbols = []
    labels = []
    functions = []
    cur = 0
    tokens = []

    def parse(self):
        self.peek()
        pass
    def statement(self):
        pass
    def expression(self):
        pass
    def nextToken(self):
        pass
    def peek(self):
        if self.cur < len(self.tokens):
            return self.tokens[self.cur + 1]
        return ""
