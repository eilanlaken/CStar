from enum import Enum
import re


class AutoName(Enum):
    def _generate_next_value_(self, name, start, count, last_values):
        return name


# token tuple: (index, regex, can it be used as a keyword?)
class TokenType(AutoName):

    # identifiers. NOTE: this allows, for example, (while) to be an identifier. Must consider these cases.
    # identifiers cannot start with _. _ is reserved for internal language processing.
    Identifier = (0, re.compile('\\b[a-zA-Z]+[a-zA-Z0-9_]*\\b'), False)

    # linker
    Read = (1, re.compile(r'\bread\b'), True)
    Page = (2, re.compile(r'\bpage\b'), True)
    Chapter = (3, re.compile(r'\bchapter\b'), True)
    Book = (4, re.compile(r'\bbook\b'), True)
    Library = (5, re.compile(r'\blibrary\b'), True)

    # omitted
    BlockCommentOpen = (6, re.compile(r'\/\*'), False)
    BlockCommentClose = (7, re.compile(r'\*\/'), False)
    LineComment = (8, re.compile(r'//'), False)
    WhiteSpace = (9, re.compile('[\s]'), False)
    Tab = (10, re.compile(r'\t'), False)
    NewLine = (11, re.compile(r'\n'), False)

    # symbols and operators
    OpenBrace = (12, re.compile(r'\('), False)
    CloseBrace = (13, re.compile(r'\)'), False)
    Semicolon = (14, re.compile(r'\;'), False)
    Colon = (15, re.compile(r'\:'), False)
    QuestionMark = (16, re.compile(r'\?'), False)
    Comma = (17, re.compile(r'\,'), False)
    OpenCurlyBrace = (18, re.compile(r'\{'), False)
    CloseCurlyBrace = (19, re.compile(r'\}'), False)
    OpenSquareBracket = (20, re.compile(r'\['), False)
    CloseSquareBracket = (21, re.compile(r'\]'), False)

    New = (22, re.compile(r'\bnew\b'), True)
    Dot = (23, re.compile(r'\.'), False)
    Assign = (24, re.compile(r'\='), False)
    AssignPlus = (25, re.compile(r'\+\='), False)
    AssignMultiply = (26, re.compile(r'\*\='), False)
    AssignMinus = (27, re.compile(r'\-\='), False)
    AssignDivide = (28, re.compile(r'\/\='), False)
    AssignReminder = (29, re.compile(r'\%\='), False)
    Plus = (30, re.compile(r'\+'), False)
    PlusPlus = (31, re.compile(r'\+\+'), False)
    Minus = (32, re.compile(r'\-'), False)
    MinusMinus = (33, re.compile(r'\-\-'), False)
    Multiply = (34, re.compile(r'\*'), False)
    Divide = (35, re.compile(r'\/'), False)
    Reminder = (36, re.compile(r'\%'), False)
    ShiftLeft = (37, re.compile(r'\<\<'), False)
    ShiftRight = (38, re.compile(r'\>\>'), False)
    And = (39, re.compile(r'\band\b'), True)
    Or = (40, re.compile(r'\bor\b'), True)
    Not = (41, re.compile(r'\bnot\b'), True)

    CompareEqual = (42, re.compile(r'\=\='), False)
    CompareNotEqual = (43, re.compile(r'\!\='), False)
    LessThan = (44, re.compile(r'\<'), False)
    GreaterThan = (45, re.compile(r'\>'), False)
    LessThanEqual = (46, re.compile(r'\<\='), False)
    GreaterThanEqual = (47, re.compile(r'\>\='), False)

    BitwiseAnd = (48, re.compile(r'\&'), False)
    BitwiseOr = (49, re.compile(r'\|'), False)
    BitwiseNot = (50, re.compile(r'\~'), False)
    BitwiseXor = (51, re.compile(r'\^'), False)

    # literals
    IntBinaryLiteral = (52, re.compile(r'\b[+-]?[^\S]*[01]+b\b'), False)
    IntLiteral = (53, re.compile(r'\b[+-]?[^\S]*[0-9]+\b'), False)
    IntHexLiteral = (54, re.compile(r'\b[+-]?[^\S]*[0-9A-F]+h\b'), False)
    FloatDecimalLiteral = (55, re.compile(r'\b([+-]?[^\S]*[0-9]+)[.][0-9]+\b'), False)
    DoubleDecimalLiteral = (56, re.compile(r'\b([+-]?[^\S]*[0-9]+)[.][0-9]+d\b'), False)
    BooleanLiteral = (57, re.compile(r'\b(true|false)\b'), False)
    CharLiteral = (58, re.compile(r'\b(\'[\w]\')|(\' \')|(\'\\[nt\\\'\"]\')\b'), False)
    StringLiteral = (59, re.compile(r'\b\"(([\w])|( )|(\\[nt\\\'\"]))+\"\b'), False)
    Null = (60, re.compile(r'\bnull\b'), False)

    # control flow
    If = (61, re.compile(r'\bif\b'), True)
    Else = (62, re.compile(r'\belse\b'), True)
    ElseIf = (63, re.compile(r'\belse[^\S]+if\b'), True)
    While = (64, re.compile(r'\bwhile\b'), True)
    Do = (65, re.compile(r'\bdo\b'), True)
    For = (66, re.compile(r'\bfor\b'), True)
    DotDotDot = (67, re.compile(r'\.\.\.'), False)
    Step = (68, re.compile(r'\bstep\b'), True)
    Break = (68, re.compile(r'\bbreak\b'), True)
    Continue = (69, re.compile(r'\bcontinue\b'), True)
    Ignore = (70, re.compile(r'\bignore\b'), True)

    # access modifiers and qualifiers
    Public = (71, re.compile(r'\bpublic\b'), True)
    Private = (72, re.compile(r'\bprivate\b'), True)
    Shared = (73, re.compile(r'\bshared\b'), True)
    Constant = (74, re.compile(r'\bconstant\b'), True)

    # functions
    Function = (75, re.compile(r'\bfunction\b'), True)
    Returns = (76, re.compile(r'\breturns\b'), True)
    Return = (77, re.compile(r'\breturn\b'), True)
    SameAs = (78, re.compile(r'\bsame[^\S]+as\b'), True)

    # object oriented model - no inheritance. class composition instead.
    Class = (79, re.compile(r'\bclass\b'), True)
    Catalog = (80, re.compile(r'\bcatalog\b'), True)
    # PartialClass = (81, re.compile(r'\bpartial[^\S]+class\b'), True) // no partial classes
    Extends = (82, re.compile(r'\bextends\b'), True)
    # Terminal = (83, re.compile(r'\bterminal\b'), True) // no terminal classes
    # PartOf = (84, re.compile(r'\bpart[^\S]+of\b'), True)  # casting the [] is the "part of" operator.
    Is = (85, re.compile(r'\bis\b'), True)
    Interface = (86, re.compile(r'\binterface\b'), True)
    TypeOf = (87, re.compile(r'\btypeof\b'), True)
    PrimitiveClass = (88, re.compile(r'\bprimitive[^\S]+class\b'), True)
    Entity = (89, re.compile(r'\bentity\b'), True)
    Relation = (90, re.compile(r'\brelation\b'), True)

    # language primitives
    Int = (91, re.compile(r'\bint\b'), True)
    Float = (92, re.compile(r'\bfloat\b'), True)
    Double = (93, re.compile(r'\bdouble\b'), True)
    Char = (94, re.compile(r'\bchar\b'), True)
    Boolean = (95, re.compile(r'\bboolean\b'), True)

    # synchronization
    Atomic = (96, re.compile(r'\batomic\b'), True)

    # annotations
    At = (97, re.compile(r'\@'), False)


