from Identifier import Identifier, DeclarationType
from JavaParser import *
from JavaParserListener import JavaParserListener


class Listener(JavaParserListener):
    def __init__(self, currentFile, fileNames, executer):
        self.out = []
        self.currentFile = currentFile
        self.fileName = fileNames
        self.executer = executer

    def enterIdentifier(self, ctx: JavaParser.IdentifierContext):
        identifier = None
        match ctx.parentCtx.getRuleIndex():
            case 7:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        None,
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.CLASS,
                                        ctx.getChild(0).getText())
            case 11:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        None,
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.ENUM,
                                        None)
            case 20:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        None,
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.METHOD,
                                        ctx.parentCtx.getChild(0).getText())
            case 38:
                identifier = self.create_variable_identifier(ctx)
            case 13:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        None,
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.ENUM_CONSTANT,
                                        ctx.parentCtx.parentCtx.parentCtx.getChild(1).getText())
            case 15:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        None,
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.INTERFACE,
                                        None)
            case 35:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        None,
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.INTERFACE_COMMON,
                                        ctx.parentCtx.getChild(0).getText())
            case 31:
                identifier = Identifier(ctx.getChild(0).getText(),
                                        ctx.parentCtx.parentCtx.getChild(2).getText(),
                                        self.fileName,
                                        ctx.start.line,
                                        DeclarationType.CONSTANT,
                                        ctx.parentCtx.parentCtx.parentCtx.parentCtx.getChild(0).getText())
        if identifier is not None:
            self.executer.identifiers.append(identifier)

    def create_variable_identifier(self, ctx):
        obj = Identifier(ctx.getChild(0).getText(),
                         None,
                         self.fileName,
                         ctx.start.line,
                         DeclarationType.VARIABLE,
                         ctx.parentCtx.parentCtx.parentCtx.parentCtx.getChild(0).getText())
        if ctx.parentCtx.parentCtx.getChildCount() == 3:
            obj.value = ctx.parentCtx.parentCtx.getChild(2).getText()
        if ctx.parentCtx.parentCtx.getChildCount() == 2:
            obj.varOrReturnType = ctx.parentCtx.parentCtx.getChild(0).getText()
        return obj
