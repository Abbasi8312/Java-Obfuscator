import os

import JavaLexer
import JavaParser


class Executer:
    def __init__(self, files):
        self.fileNames, self.filePaths = files
        self.extractor = None
        self.renamer = None
        self.fileCopies = []
        self.identifiers = []

    @staticmethod
    def readJavaFile(filepath: str):
        context = None
        readingJavaFile = filepath
        try:
            context = open(readingJavaFile, "r")
        except IOError:
            print("Something went wronged reading the file")
        return context.read()

    def executeFiles(self):
        self.makeTable()

    def makeTable(self):
        for i in range(len(self.filePaths)):
            input_text = self.readJavaFile(os.path.join(self.filePaths[i], self.fileNames[i]))
            input_stream = JavaParser.InputStream(input_text)
            lexer = JavaLexer(input_stream)
            stream = JavaParser.CommonTokenStream(lexer)
            parser = JavaParser.JavaParser(stream)
            tree = parser.compilationUnit()  # Parse the entire compilation unit

            walker = JavaParser.ParseTreeWalker()
            walker.walk(self.extractor, tree)
            fileCopy = ' '.join(self.extractor.out)
            self.fileCopies.append(fileCopy)
