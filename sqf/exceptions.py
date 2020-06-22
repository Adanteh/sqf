from sqf.context_writer import Context


"""
Raised by the parser and analyzer
"""
class SQFError(Exception):
    level = ''

    def __init__(self, context: Context, message: str):
        self.context = context
        self.message = message.replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r")


"""
Raised by the parser and analyzer
"""
class SQFParserError(SQFError):
    level = 'error'


class SQFParenthesisError(SQFParserError):
    pass


"""
Something that the interpreter understands but that is a bad practice or potentially
semantically incorrect.
"""
class SQFWarning(SQFError):
    level = 'warning'
