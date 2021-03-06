from antlr4 import CommonTokenStream, InputStream

if __name__ == '__main__':
    from python.Python3Parser import Python3Parser
    from python.Python3Lexer import Python3Lexer
    from python.Python3Visitor import Python3Visitor
else:
    from python.antlr.python.Python3Parser import Python3Parser
    from python.antlr.python.Python3Lexer import Python3Lexer
    from python.antlr.python.Python3Visitor import Python3Visitor


class Visitor(Python3Visitor):
    def __init__(self):
        self.words = set()

    def visitFuncdef(self, ctx):
        word = ctx.getChild(1).getText()
        self.words.add(word)
        return self.visitChildren(ctx)

    def visitClassdef(self, ctx):
        word = ctx.getChild(1).getText()
        self.words.add(word)
        return self.visitChildren(ctx)


def get_words_from_python(text):
    lexer = Python3Lexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    if parser.getNumberOfSyntaxErrors() != 0:
        print("File contains {} "
              "syntax errors".format(parser.getNumberOfSyntaxErrors()))
        return list()

    visitor = Visitor()
    visitor.visit(tree)
    return list(visitor.words)


if __name__ == '__main__':
    with open("/Users/oliverwidder/Documents/dev/erp_doc/erpnext/code/healthcare/doctype/patient_appointment/patient_appointment.py", "r") as file:
        text = file.read()
        l = get_words_from_python(text)
        print(str(l))

