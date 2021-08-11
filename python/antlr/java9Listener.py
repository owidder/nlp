from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker


if __name__ == '__main__':
    from java9.Java9Lexer import Java9Lexer
    from java9.Java9Parser import Java9Parser
    from java9.Java9ParserListener import Java9ParserListener
else:
    from python.antlr.java9.Java9Lexer import Java9Lexer
    from python.antlr.java9.Java9Parser import Java9Parser
    from python.antlr.java9.Java9ParserListener import Java9ParserListener


class Java9Listener(Java9ParserListener):

    def enterClassDeclaration(self, ctx:Java9Parser.ClassDeclarationContext):
        print(ctx.getText())


def start(text):
    lexer = Java9Lexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = Java9Parser(stream)
    tree = parser.compilationUnit()
    java9Listener = Java9Listener()
    walker = ParseTreeWalker()
    walker.walk(java9Listener, tree)


if __name__ == '__main__':
    with open("/Users/oliverwidder/Documents/dev/erp_doc/axelor-open-suite/axelor-business-project/src/main/java/com/axelor/apps/businessproject/web/ProjectFolderController.java", "r") as file:
        text = file.read()
        start(text)
