def check_syntax(line, line_number):
    try:
        if line == '\n':
            return 'skip'
        elif '//' in line:
            sudo_line = line.split( "//" )
            line = ""

            for times_ran, semicolon_splits in enumerate( sudo_line, start = 0 ):

                if times_ran % 2 == 0:

                    line = line + semicolon_splits

            if line == '':

                return 'skip'

        line = line.strip( )
        split_line = line.split( ";" )
        first_line = split_line[ 0 ]
        second_line = split_line[ 1 ].strip( '' )
        second_line = second_line.replace( '\n', '' )

        if second_line != '':

            print( "\033[31m" + "Invalid Syntax " + " Line " + str( line_number ) + ": " + line.replace( '\n', '' ) )
            exit( )

        return first_line

    except IndexError:
        print( "\033[31m" + "Invalid Syntax " + " Line " + str( line_number ) + ": " + line.replace( '\n', '' ) )
        print( "\033[31m" + "Possibly missing a semicolon" )
        exit( )


def using_statement():
    pass

def skip(code):
    if code == 'skip':
        return True


def import_function(code, line_number):
    if code.startswith("using "):
        code = code[len("using "):]
        try:
            __import__(code)
            return 'skip'
        except ModuleNotFoundError:
            print("\033[31m" + "Line " + str(line_number) + ": Could not find module: " + code)
            print("\033[31m" + "    Type " + "\033[36m" + "module help" + "\033[31m" + " for a list of modules")
            exit()
    else:
        return code

def module_help(line, line_number):
    if line.strip().lower() == 'module help':
        print("\033[34m" + "Module Help was called on line " + str(line_number))
        modules = ["console", "mouse", "loop", "pyautogui", "MORE TO COME"]
        try:
            type_list_print = int(input("1 for list, 2 for new line strings: "))
            if type_list_print == 1:
                print("Outputting list of modules")
                print(modules)
            elif type_list_print == 2:
                print("Outputting new line strings of modules")
                for module in modules:
                    print(module)
            else:
                print("\033[31m" + "Please enter only numbers 1 or 2")
        except ValueError:
            print("\033[31m" + "Please enter only numbers 1 or 2")