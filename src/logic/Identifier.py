from enum import Enum


class DeclarationType(Enum):
    CLASS = "classDeclaration"
    ENUM = "enumDeclaration"
    METHOD = "methodDeclaration"
    VARIABLE = "variableDeclaratorID"
    ENUM_CONSTANT = "enumConstant"
    INTERFACE = "interfaceDeclaration"
    CONSTANT = "constantDeclarator"
    INTERFACE_COMMON = "interfaceCommonBodyDeclaration"


class Identifier:

    def __init__(self, name, value, file_name, line, declaration_type, var_or_return_type):
        self.name = name
        self.value = value
        self.fileName = file_name
        self.line = line
        self.type = declaration_type
        self.varOrReturnType = var_or_return_type
