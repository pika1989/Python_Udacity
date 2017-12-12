"""Simple Daikon-style invariant checker."""


import sys
import math
import random


def square_root(x, eps=0.00001):
    assert x > 0
    y = math.sqrt(x)
    assert abs(square(y) - x) <= eps
    return y


def square(x):
    return x * x


def double(x):
    return abs(20 * x) + 10


class Range(object):
    
    """Tracks the types and value ranges for a single variable."""

    def __init__(self):
        self.min = None
        self.max = None
        self.type = None
        self.set = set()

    def track(self, value):
        if not self.min and not self.max:
            self.min = value
            self.max = value
        elif value > self.max:
            self.max = value
        elif value < self.min:
            self.min = value
        
        self.set.add(value)
        self.type = type(value)

    def __repr__(self):
        return '%s %s..%s %s' % (repr(self.type),
                                 repr(self.min),
                                 repr(self.max),
                                 repr(self.set))


class Invariants:
    
    """Tracks all Ranges for all variables seen."""

    def __init__(self):
        """Mapping (Function Name) -> (Event type) -> (Variable Name)
        e.g. self.vars["sqrt"]["call"]["x"] = Range()
        holds the range for the argument x when calling sqrt(x)
        """
        self.vars = {}

    def track(self, frame, event, arg):
        if event == 'call' or event == 'return':
            #get the function name
            func_name = frame.f_code.co_name
            loc_vars = frame.f_locals

            #get the dictionary related to this function
            dict_func = self.vars.get(func_name)
            
            if dict_func is None:
                dict_func = {}
                dict_func['call'] = {}
                dict_func['return'] = {}
                self.vars[func_name] = dict_func

            if arg is not None:
                range = dict_func[event].get('ret')
                if range is None:
                    range = Range()
                    dict_func[event]["ret"] = range
                    range.track(arg)
            
            for var in loc_vars:
                range = dict_func[event].get(var)
                if range is None:
                    range = Range()
                    dict_func[event][var] = range
                range.track(loc_vars[var])

    def __repr__(self):
        """Returns the tracked invariants."""
        s = ''
        for function, events in self.vars.iteritems():
            for event, vars in events.iteritems():
                s += event + ' ' + function + ':\n'

                for var, range in vars.iteritems():
                    s += '    assert isinstance(%s, type(%s))\n' % (var, repr(range.min))
                    s += '    assert %s in %s\n' % (var, str(range.set))
                    s += '    assert '
                    if range.min == range.max:
                        s += '%s == %s\n' % (var, repr(range.min))
                    else:
                        s += '%s <= %s <= %s\n' % (repr(range.min), var, repr(range.max))
                    for var2, range2 in vars.iteritems():
                        if var2 is not var:
                            if (range.min == range2.min) and (range.max == range2.max):
                                op = '=='
                            if range.min <= range2.min:
                                op = '<='
                            else:
                                op = '>='
                            s += '    assert %s %s %s\n' % (var, op, var2)

        return s


invariants = Invariants()

def traceit(frame, event, arg):
    invariants.track(frame, event, arg)
    return traceit


sys.settrace(traceit)
eps = 0.000001
test_vars = [34.6363, 9.348, -293438.402, 3, 0, -10]

for i in test_vars:
    r = int(random.random() * 1000)
    z = square_root(r, eps)
    z = square(z)
    z = double(i)

sys.settrace(None)
print invariants
