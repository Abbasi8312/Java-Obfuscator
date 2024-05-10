import os

from prettytable import PrettyTable

from JavaLexer import JavaLexer
from Listener import *


class Extractor:
    def __init__(self, files):
        self.fileNames, self.filePaths = files
        self.extractor = None
        self.renamer = None
        self.fileCopies = []
        self.identifiers = []

    @staticmethod
    def read_file(java_file_path):
        context = None
        try:
            context = open(java_file_path, "r")
        except IOError:
            print("Error reading the file")
        return context.read()

    def extract(self):
        self.extract_tokens()
        self.show_table()

    def extract_tokens(self):
        for i in range(len(self.filePaths)):
            input_text = self.read_file(os.path.join(self.filePaths[i], self.fileNames[i]))
            input_stream = InputStream(input_text)
            lexer = JavaLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = JavaParser(stream)
            tree = parser.compilationUnit()  # Parse the entire compilation unit
            self.extractor = Listener(self.filePaths[i], self.fileNames[i], self)
            walker = ParseTreeWalker()
            walker.walk(self.extractor, tree)
            file_copy = ' '.join(self.extractor.out)
            self.fileCopies.append(file_copy)

    def show_table(self):
        table = PrettyTable(["Name", "Value", "FileName", "Line", "Type", "Var or ReturnType"])
        for i in range(len(self.identifiers)):
            table.add_row([self.identifiers[i].name, self.identifiers[i].value if self.identifiers[i].value else '-',
                           self.identifiers[i].fileName, self.identifiers[i].line, self.identifiers[i].type.value,
                           self.identifiers[i].varOrReturnType if self.identifiers[i].varOrReturnType else '-'])
        print(table)
