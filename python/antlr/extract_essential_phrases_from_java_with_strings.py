from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from typing import TextIO
import sys


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

    def enterInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
         self.essential_phrases.append(ctx.getChild(1).getText())

    def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
         self.essential_phrases.append(ctx.getChild(1).getText())


class StringJavaLexer(JavaLexer):
    def __init__(self, essential_phrases: [], input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.essential_phrases = essential_phrases

    def emitToken(self, t):
        super().emitToken(t)
        if t.type == JavaLexer.STRING_LITERAL:
            self.essential_phrases.append(t.text)


def extract_essential_phrases_from_java(source_code: str) -> [str]:
    essential_phrases = []
    lexer = StringJavaLexer(essential_phrases, InputStream(source_code))
    parser = JavaParser(CommonTokenStream(lexer))
    ParseTreeWalker().walk(JavaListener(essential_phrases), parser.compilationUnit())

    return essential_phrases
