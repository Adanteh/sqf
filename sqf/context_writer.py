import copy


class AnalysisWriter:

    _previousFile = ''

    def __init__(self, writer):
        self.writer = writer

    def log(self, context, level, message):
        topmost_file = ''
        if context.include_stack:
            topmost_file = context.include_stack[-1]
        if self._previousFile != topmost_file:
            self.writer.write('%s%s\n' % (''.rjust(len(context.include_stack) - 1), topmost_file))
            self._previousFile = topmost_file
        indent = ''
        if topmost_file != '':
            indent = '\t'
        self.writer.write('%s[%d,%d]:%s:%s\n' % (indent, context.line, context.col - 1, level, message))

    def warn(self, context, message):
        self.log(context, 'warning', message)

    def error(self, context, message):
        self.log(context, 'error', message)


class Context:
    include_stack = []
    line = 0
    col = 0

    def __init__(self, file_name=''):
        if file_name != '':
            self.include_stack = [file_name]

    def push_include(self, file_name: str) -> 'Context':
        new = self.with_position((0, 0))
        new.include_stack = copy.copy(self.include_stack).append(file_name)

        return new

    def with_position(self, position: (int, int)) -> 'Context':
        new = copy.copy(self)
        new.line = position[0]
        new.col = position[1]
        return new
