from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
import sys
from typing import TextIO


from python.antlr.python.Python3Parser import Python3Parser
from python.antlr.python.Python3Lexer import Python3Lexer
from python.antlr.python.Python3Listener import Python3Listener


class PythonListener(Python3Listener):
    def __init__(self, essential_phrases):
        self.essential_phrases = essential_phrases

    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        self.essential_phrases.append(ctx.getChild(1).getText())


class StringPythonLexer(Python3Lexer):

    def __init__(self, essential_phrases: [], input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.essential_phrases = essential_phrases

    def emitToken(self, token):
        super().emitToken(token)
        if token.type == Python3Lexer.STRING or token.type == Python3Lexer.STRING_LITERAL:
            self.essential_phrases.append(token.text)


def extract_essential_phrases_from_python(source_code: str) -> [str]:
    essential_phrases = []
    lexer = StringPythonLexer(essential_phrases, InputStream(source_code))
    parser = Python3Parser(CommonTokenStream(lexer))
    ParseTreeWalker().walk(PythonListener(essential_phrases), parser.file_input())

    return essential_phrases
