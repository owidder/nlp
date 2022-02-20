from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
import sys
from typing import TextIO


from python.antlr.python.Python3Parser import Python3Parser
from python.antlr.python.Python3Lexer import Python3Lexer
from python.antlr.python.Python3Listener import Python3Listener


class PythonListener(Python3Listener):
    def __init__(self, essential_words):
        self.essential_words = essential_words

    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        self.essential_words.append(ctx.getChild(1).getText())

    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        self.essential_words.append(ctx.getChild(1).getText())


class StringPythonLexer(Python3Lexer):

    def __init__(self, words: [], input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.words = words

    def emitToken(self, t):
        super().emitToken(t)
        if t.type == Python3Lexer.STRING or t.type == Python3Lexer.STRING_LITERAL:
            self.words.append(t.text)


def extract_essential_words_from_python(source_code: str) -> str:
    essential_words = []
    lexer = StringPythonLexer(essential_words, InputStream(source_code))
    parser = Python3Parser(CommonTokenStream(lexer))
    ParseTreeWalker().walk(PythonListener(essential_words), parser.file_input())

    return " ".join(essential_words)
