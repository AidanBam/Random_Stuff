import console
import main_functions

file = open("Test code file")
for line_number, line in enumerate(file, start = 1):
    main_functions.module_help(line = line, line_number = line_number)
    code = main_functions.check_syntax(line = line, line_number = line_number)  # returns either skip or first part of code(using console) without ;
    if main_functions.skip(code) is True:
        continue
    code = main_functions.import_function(code = code, line_number = line_number) #checks if first part of code is using, if is imports that module
    if code == None:
        continue
    if code.startswith('console.'):
        code = code[len("console."):]
        console.console_check(code)

