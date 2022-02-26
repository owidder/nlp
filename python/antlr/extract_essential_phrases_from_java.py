from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker


from python.antlr.java.JavaLexer import JavaLexer
from python.antlr.java.JavaParser import JavaParser
from python.antlr.java.JavaParserListener import JavaParserListener


class JavaListener(JavaParserListener):
    def __init__(self, essential_phrases: []):
        self.essential_phrases = essential_phrases

    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        self.essential_phrases.append(ctx.getChild(1).getText())


def extract_essential_phrases_from_java(source_code: str) -> [str]:
    essential_phrases = []
    parser = JavaParser(CommonTokenStream(JavaLexer(InputStream(source_code))))
    ParseTreeWalker().walk(JavaListener(essential_phrases), parser.compilationUnit())

    return essential_phrases
