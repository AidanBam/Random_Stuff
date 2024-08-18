import console
end_of_line = ''

def console_check(code):
    if code.startswith('set.'):
        code = code[len('set.')]
        if code.startswith('newline'):
            set_new_line(code)

    elif code.startswith('writeline'):
        code = code[len("writeline"):]
        write_line(code)

    elif code.startswith("newline"):
        new_line(code)


def set_new_line(code):
    global end_of_line
    end_of_line = code
def new_line(code):
    print("\n")

def write_line(code):
    code = code.strip('(')
    code = code.strip( '"' )
    code = code.strip( ')' )
    code = code.strip('"')
    print(code, end = end_of_line)
