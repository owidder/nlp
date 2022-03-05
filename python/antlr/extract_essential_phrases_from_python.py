from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker


from python.antlr.python.Python3Parser import Python3Parser
from python.antlr.python.Python3Lexer import Python3Lexer
from python.antlr.python.Python3Listener import Python3Listener


class PythonListener(Python3Listener):

    def __init__(self):
        super().__init__()
        self.essential_phrases = []

    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        self.essential_phrases.append(ctx.getChild(1).getText())

    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        self.essential_phrases.append(ctx.getChild(1).getText())


def extract_essential_phrases_from_python(source_code: str) -> [str]:
    parser = Python3Parser(CommonTokenStream(Python3Lexer(InputStream(source_code))))
    python_listener = PythonListener()
    ParseTreeWalker().walk(python_listener, parser.file_input())

    return python_listener.essential_phrases.copy()
