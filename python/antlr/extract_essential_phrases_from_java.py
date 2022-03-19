from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker


from python.antlr.java.JavaLexer import JavaLexer
from python.antlr.java.JavaParser import JavaParser
from python.antlr.java.JavaParserListener import JavaParserListener


class JavaListener(JavaParserListener):

    def __init__(self):
        super().__init__()
        self.essential_phrases = []

    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
         self.essential_phrases.append(ctx.getChild(1).getText())


def extract_essential_phrases_from_java(source_code: str) -> [str]:
    parser = JavaParser(CommonTokenStream(JavaLexer(InputStream(source_code))))
    java_listener = JavaListener()
    ParseTreeWalker().walk(java_listener, parser.compilationUnit())

    return java_listener.essential_phrases.copy()
