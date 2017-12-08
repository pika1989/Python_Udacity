import sys


def remove_html_markup(text):
    tag = False
    quote = False
    output = ''

    for character in text:
        if character == '<' and not quote:
            tag = True
        elif character == '>' and not quote:
            tag = False
        elif (character == '"' or character == "'") and tag:
            quote = not quote
        elif not tag:
            output += character
    
    return output


stepping = False
breakpoints = {3: True}
watchpoints = {'character': True}


def debug(command, my_locals):
    global stepping                                                             
    global breakpoints
    global watchpoints

    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None

    if command.startswith('s'): # step
        stepping = True
        return True
    elif command.startswith('c'): # continue
        stepping = False
        return True
    elif command.startswith('p'): # print
        if not arg:
            print my_locals
        elif arg in my_locals:
            print '%s = %s' % (arg, repr(my_locals[arg]))
        else:
            print 'No such variable %s' % (arg)
    elif command.startswith('b'): # breakpoint
        if not arg:
            print 'You must supply a line number'
        else:
            breakpoints[int(arg)] = True
    elif command.startswith('w'): # watchpoint
        if not arg:
            print 'You must supply a variable name'
        elif arg in my_locals:
            watchpoints[arg] = True
        else:
            print 'No such variable %s' % (arg)
    elif command.startswith('q'):
        sys.exit(0)
    else:
        print 'No such command %s' % (repr(command))


commands = ['b 5', 'p', 'c', 'q']

def input_command():
    global commands
    return commands.pop(0)


def traceit(frame, event, arg):
    global stepping
    global breakpoints

    if event == 'line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            while not resume:
                print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
                command = input_command()
                resume = debug(command, frame.f_locals)

    return traceit


if __name__ == '__main__':
    sys.settrace(traceit)
    print remove_html_markup('xyz')
    print remove_html_markup('<b>foo</b>')
    print remove_html_markup('<b>"foo"</b>')
    print remove_html_markup('"<b>foo</b>"')
    print remove_html_markup('<a href=">">foo</a>')
    sys.settrace(None)
