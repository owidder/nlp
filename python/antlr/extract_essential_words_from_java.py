from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from typing import TextIO
import sys


from python.antlr.java.JavaLexer import JavaLexer
from python.antlr.java.JavaParser import JavaParser
from python.antlr.java.JavaParserListener import JavaParserListener


class JavaListener(JavaParserListener):
    def __init__(self, essential_words: []):
        self.essential_words = essential_words

    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        self.essential_words.append(ctx.getChild(1).getText())

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        self.essential_words.append(ctx.getChild(1).getText())

    def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        self.essential_words.append(ctx.getChild(1).getText())


class StringJavaLexer(JavaLexer):
    def __init__(self, essential_words: [], input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.essential_words = essential_words

    def emitToken(self, t):
        super().emitToken(t)
        if t.type == JavaLexer.STRING_LITERAL:
            self.essential_words.append(t.text)


def extract_essential_words_from_java(source_code: str) -> str:
    essential_words = []
    lexer = StringJavaLexer(essential_words, InputStream(source_code))
    parser = JavaParser(CommonTokenStream(lexer))
    ParseTreeWalker().walk(JavaListener(essential_words), parser.compilationUnit())

    return " ".join(essential_words)
