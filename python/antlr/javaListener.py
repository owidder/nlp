from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from typing import TextIO
import sys

from python.antlr.java.JavaLexer import JavaLexer
from python.antlr.java.JavaParser import JavaParser
from python.antlr.java.JavaParserListener import JavaParserListener


class JavaListener(JavaParserListener):
    def __init__(self, words: []):
        self.words = words

    def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
        word = ctx.getChild(1).getText()
        self.words.append(word)

    def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
        word = ctx.getChild(1).getText()
        self.words.append(word)

    def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
        word = ctx.getChild(1).getText()
        self.words.append(word)


class StringJavaLexer(JavaLexer):
    def __init__(self, words: [], input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.words = words

    def emitToken(self, t):
        super().emitToken(t)
        if t.type == JavaLexer.STRING_LITERAL:
            self.words.append(t.text)


def parse_words_from_java(text):
    _words = []
    lexer = StringJavaLexer(_words, InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    ParseTreeWalker().walk(JavaListener(_words), parser.compilationUnit())

    return " ".join(_words)
