from compiler.lexer.lexer import *
import context.gamecode_context as context


def __get_demo_program():
    path = r"C:\Users\User\PycharmProjects\CStar\compiler\lexer\lexer_input"
    file = open(path, "r")
    program = file.read() + '\n'
    file.close()
    return program


def __main__():
    __main__ide()


def __main__compiler_debug():
    program = __get_demo_program()
    tokens = tokenize_code(program)
    for token in tokens:
        print(token)


def __main__ide():
    print('launching ide')
    gamecode_context = context.GameCodeContext()
    gamecode_context.launch()


__main__()
