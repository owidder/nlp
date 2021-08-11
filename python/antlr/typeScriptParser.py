from antlr4 import CommonTokenStream, InputStream

if __name__ == '__main__':
    from typeScript.TypeScriptParser import TypeScriptParser
    from typeScript.TypeScriptLexer import TypeScriptLexer
    from typeScript.TypeScriptParserVisitor import TypeScriptParserVisitor
else:
    from python.antlr.typeScript.TypeScriptParser import TypeScriptParser
    from python.antlr.typeScript.TypeScriptLexer import TypeScriptLexer
    from python.antlr.typeScript.TypeScriptParserVisitor import TypeScriptParserVisitor


class Visitor(TypeScriptParserVisitor):
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
    lexer = TypeScriptLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = TypeScriptParser(stream)
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

