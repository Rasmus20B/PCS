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
        self.cur += 1
        return self.tokens[self.cur]
    def peek(self):
        if self.cur < len(self.tokens):
            return self.tokens[self.cur + 1]
        return ""
