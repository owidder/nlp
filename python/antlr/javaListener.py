from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from python.antlr.listenerGuard import ListenerGuard

if __name__ == '__main__':
    from java.JavaLexer import JavaLexer
    from java.JavaParser import JavaParser
    from java.JavaParserListener import JavaParserListener
else:
    from python.antlr.java.JavaLexer import JavaLexer
    from python.antlr.java.JavaParser import JavaParser
    from python.antlr.java.JavaParserListener import JavaParserListener


class JavaListener(JavaParserListener):
    def __init__(self, words: []):
        self.words = words
        self.identifierGuard = ListenerGuard()

    def exitEveryRule(self, ctx):
        self.identifierGuard.end_open_or_close()

    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        self.identifierGuard.open_gate()

    def enterAnnotation(self, ctx:JavaParser.AnnotationContext):
        self.identifierGuard.close_gate()

    def enterClassBody(self, ctx:JavaParser.ClassBodyContext):
        self.identifierGuard.close_gate()

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        self.identifierGuard.open_gate()

    def enterTypeParameters(self, ctx:JavaParser.TypeParametersContext):
        self.identifierGuard.close_gate()

    def enterFormalParameterList(self, ctx:JavaParser.FormalParameterListContext):
        self.identifierGuard.close_gate()

    def enterMethodBody(self, ctx:JavaParser.MethodBodyContext):
        self.identifierGuard.close_gate()


def start(text):
    _words = []
    lexer = JavaLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    ParseTreeWalker().walk(JavaListener(_words), parser.compilationUnit())

    return " ".join(_words)

if __name__ == '__main__':
    with open("/Users/oliverwidder/Documents/dev/erp_doc/axelor-open-suite/axelor-business-project/src/main/java/com/axelor/apps/businessproject/web/ProjectFolderController.java", "r") as file:
        text = file.read()
        start(text)
