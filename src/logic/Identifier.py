from enum import Enum


class DeclarationType(Enum):
    CLASS = "7"
    ENUM = "11"
    METHOD = "20"
    VARIABLE = "38"
    ENUM_CONSTANT = "13"
    INTERFACE = "15"
    CONSTANT = "31"
    INTERFACE_COMMON = "35"


class Identifier:

    def __init__(self, name, value, file_name, line, declaration_type, var_or_return_type):
        self.name = name
        self.value = value
        self.fileName = file_name
        self.line = line
        self.type = declaration_type
        self.varOrReturnType = var_or_return_type
