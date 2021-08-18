from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
import sys
from typing import TextIO

if __name__ == '__main__':
    from python.Python3Parser import Python3Parser
    from python.Python3Lexer import Python3Lexer
    from python.Python3Listener import Python3Listener
else:
    from python.antlr.python.Python3Parser import Python3Parser
    from python.antlr.python.Python3Lexer import Python3Lexer
    from python.antlr.python.Python3Listener import Python3Listener


class PythonListener(Python3Listener):
    def __init__(self, words):
        self.words = words

    def enterFuncdef(self, ctx:Python3Parser.FuncdefContext):
        word = ctx.getChild(1).getText()
        self.words.append(word)

    def enterClassdef(self, ctx:Python3Parser.ClassdefContext):
        word = ctx.getChild(1).getText()
        self.words.append(word)


class StringPythonLexer(Python3Lexer):

    def __init__(self, words: [], input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.words = words

    def emitToken(self, t):
        super().emitToken(t)
        if t.type == Python3Lexer.STRING or t.type == Python3Lexer.STRING_LITERAL:
            self.words.append(t.text)


def parse_words_from_python(text: str) -> str:
    _words = []
    lexer = StringPythonLexer(_words, InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    ParseTreeWalker().walk(PythonListener(_words), parser.file_input())

    return " ".join(_words)


if __name__ == '__main__':
    with open("/Users/oliverwidder/Documents/dev/erp_doc/erpnext/code/healthcare/doctype/patient_appointment/patient_appointment.py", "r") as file:
        text = file.read()
        words = parse_words_from_python(text)
        print(words)
