from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker


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


def extract_essential_phrases_from_python(source_code: str) -> [str]:
    essential_phrases = []
    parser = Python3Parser(CommonTokenStream(Python3Lexer(InputStream(source_code))))
    ParseTreeWalker().walk(PythonListener(essential_phrases), parser.file_input())

    return essential_phrases
