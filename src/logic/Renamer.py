from Identifier import Identifier, DeclarationType
from JavaParser import *
from JavaParserListener import JavaParserListener


class Renamer(JavaParserListener):
    def __init__(self, currentFile, fileNames, extractor):
        self.out = []
        self.currentFile = currentFile
        self.fileName = fileNames
        self.extractor = extractor
        self.types_map = {7: [7, 51, 104, 25, 111, 82], 11: [11, 104, 82, 51], 20: [20, 98, 99], 38: [38, 104, 99, 98],
                          13: [13, 99, 104], 15: [15, 51, 82], 35: [35, 98, 20], 31: [31, 104]}

    def enterIdentifier(self, ctx: JavaParser.IdentifierContext):
        type = ctx.parentCtx.getRuleIndex()
        # print(ctx.getText(), self.currentFile)
        # print(ctx.getText(),ctx.parentCtx.getRuleIndex(),ctx.start.line)
        for id in self.extractor.identifiers:
            self.change_id_name(id, ctx, type)

    def enterTypeIdentifier(self, ctx: JavaParser.TypeIdentifierContext):
        type = ctx.getRuleIndex()
        for id in self.extractor.identifiers:
            self.change_id_name(id, ctx, type)

    def change_id_name(self, id: Identifier, ctx, type):
        name = ctx.getText()
        token = ctx.start

        if id.name == name:
            if name == "main" and id.type == DeclarationType.METHOD:
                return
            # if id.type == 7 and type not in self.types_map[id.type]:
            #     print("-------------------------------------------------")
            #     print(self.currentFile, name, type, token.line)
            # print(id.type)
            if type in self.types_map[int(id.type.value)]:
                # if name not in self.extractor.should_ignore_classes:
                pascal_case_name = name[0].upper() + name[1:]
                if id.type == DeclarationType.CLASS:
                    token.text = f'New{pascal_case_name}'
                else:
                    token.text = f'new{pascal_case_name}'  # print(token.text)

    def visitTerminal(self, node):
        token = node.symbol
        if token is not None:
            self.out.append(token.text)
        return super().visitTerminal(node)
