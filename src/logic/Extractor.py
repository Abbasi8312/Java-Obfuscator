import os

from prettytable import PrettyTable

from JavaLexer import JavaLexer
from Listener import *
from src.logic.Renamer import Renamer


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
        self.rename_tokens()

    def extract_tokens(self):
        for i in range(len(self.filePaths)):
            input_text = self.read_file(os.path.join(self.filePaths[i], self.fileNames[i]))
            tree = self.init_parser(input_text)
            self.extractor = Listener(self.filePaths[i], self.fileNames[i], self)
            walker = ParseTreeWalker()
            walker.walk(self.extractor,
                        tree)  # file_copy = ' '.join(self.extractor.out)  # self.fileCopies.append(file_copy)

    def rename_tokens(self):
        for i in range(len(self.filePaths)):
            input_text = self.read_file(os.path.join(self.filePaths[i], self.fileNames[i]))
            tree = self.init_parser(input_text)
            self.renamer = Renamer(self.filePaths[i], self.fileNames[i], self)
            walker = ParseTreeWalker()
            walker.walk(self.renamer, tree)
            file_copy = ' '.join(self.renamer.out)
            self.fileCopies.append(file_copy)
            self.make_output(i, file_copy)

    def init_parser(self, input_text):
        input_stream = InputStream(input_text)
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()  # Parse the entire compilation unit
        return tree

    def show_table(self):
        table = PrettyTable(["Name", "Value", "FileName", "Line", "Type", "Var or ReturnType"])
        for i in range(len(self.identifiers)):
            table.add_row([self.identifiers[i].name, self.identifiers[i].value if self.identifiers[i].value else '-',
                           self.identifiers[i].fileName, self.identifiers[i].line, self.identifiers[i].type.name,
                           self.identifiers[i].varOrReturnType if self.identifiers[i].varOrReturnType else '-'])
        print(table)

    def make_output(self, i, final_output_with_replaced_classes):
        java_file_name = f'New{self.fileNames[i][0].upper() + self.fileNames[i][1:]}'
        # print(self.filePaths[i])
        # write_path = self.filePaths[i].replace('aliProject', 'src')
        write_path = "..\\..\\output"
        if not os.path.exists(write_path):
            os.makedirs(write_path)
        with open(os.path.join(write_path, java_file_name), "w") as java_file:
            # print(os.path.join(write_path, java_file_name))
            java_file.write(final_output_with_replaced_classes)
