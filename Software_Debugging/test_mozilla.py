import re

def remove_html_markup(text):
    tag = False
    quote = False
    output = ''

    for character in text:
        if character == '<' and not quote:
            tag = True
        elif character == '>' and not quote:
            tag = False
        elif character == '"' or character == "'" and tag:
            quote = not quote
        elif not tag:
            output += character

    assert output.find('<') == -1
    return output


test_count = 0

def test(s):
    """Returns 'FAIL' if s causes Mozilla to crash, otherwise 'PASS'"""
    global test_count
    test_count = test_count + 1
    print test_count, repr(s), len(s),

#    if re.search('<SELECT[^>]*>', s) >= 0:
#        print 'FAIL'
#        return 'FAIL'
#    else:
#        print 'PASS'
#        return 'PASS'
    try:
        result = remove_html_markup(s)
        print 'PASS'
        return 'PASS'
    except AssertionError:
        print 'FAIL'
        return 'FAIL'


def simplify(s):
    assert test(s) == 'FAIL'

    print repr(s), len(s)

    split = len(s) / 2
    s1 = s[:split]
    s2 = s[split:]

    assert s == s1 + s2

    if test(s1) == 'FAIL':
        return simplify(s1)
    if test(s2) == 'FAIL':
        return simplify(s2)
        
    return s


def ddmin(s):
    assert test(s) == 'FAIL'
    
    n = 2 # Initial granularity
    while len(s) >= 2:
        start = 0
        subset_length = len(s) / n
        some_complement_is_failing = False

        while start < len(s):
            complement = s[:start] + s[start + subset_length:]
            if test(complement) == 'FAIL':
                s = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break
            
            start += subset_length
        
        if not some_complement_is_failing:
            n = min(n * 2, len(s))
            if len(s) == n:
                break

    return s


#html_input = '<SELECT><OPTION VALUE="simplify"><OPTION VALUE="beautify"></SELECT>'
#html_input = '<SELECT>foo</SELECT>'
html_input = '"<b>foo</b>"'
#print simplify(html_input)
print ddmin(html_input)
