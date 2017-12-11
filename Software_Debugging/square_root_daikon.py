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
        if not self.min and not self.max and not self.type:
            self.min = value
            self.max = value
            self.type = type(value)
        elif value > self.max:
            self.max = value
        elif value < self.min:
            self.min = value
        
        if value not in self.set:
            self.set.add(value)

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
            f = frame.f_code.co_name
            loc_vars = frame.f_locals
            
            if f not in self.vars:
                self.vars[f] = {}
            
            if event not in self.vars[f]:
                self.vars[f][event] = {}
            
            if event == 'return':
                if 'ret' not in self.vars[f][event]:
                    r = Range()
                    r.track(arg)
                    self.vars[f][event]['ret'] = r
                else:
                    self.vars[f][event]['ret'].track(arg)
            else:
                for var in loc_vars.keys():
                    if var not in self.vars[f][event]:
                        r = Range()
                        r.track(loc_vars[var])
                        self.vars[f][event][var] = r
                    else:
                        self.vars[f][event][var].track(loc_vars[var])

    def __repr__(self):
        """Returns the tracked invariants."""
        s = ''
        for function, events in self.vars.iteritems():
            for event, vars in events.iteritems():
                s += event + ' ' + function + ':\n'

                for var, range in vars.iteritems():
                    s += '    assert isinstance(' + var + ', type(' + vars[function][event][var] + '))'
                    s += '    assert '
                    if range.min == range.max:
                        s += var + ' == ' + repr(range.min)
                    else:
                        s += repr(range.min) + ' <= ' + var + ' <= ' + repr(range.max)
                    s += '\n'
                    s += '    assert ' + var + ' >= ' + var2 + '\n'

        return s


invariants = Invariants()

def traceit(frame, event, arg):
    invariants.track(frame, event, arg)
    return traceit


sys.settrace(traceit)
eps = 0.000001
test_vars = [34.6363, 9.348, -293438.402]

for i in test_vars:
#for i in range (1, 10):
#    r = int(random.random() * 1000)
#    z = square_root(r, eps)
#    z = square(z)
    z = double(i)

sys.settrace(None)
print invariants
