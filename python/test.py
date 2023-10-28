class MyTests(TestCase):
     def test_something_python2(self):
        self.failUnlessEqual(1, 1)

def set_literals_python2():
    s = set([1, 2, 3])
    return s

def dictionary_comprehensions_python2():
    d = dict((a, b) for a, b in y)
    return d

def format_specifiers_python2():
    s = '{0} {1}'.format(1, 2)
    return s

def printf_style_string_formatting_python2(a, b):
    s = '%s %s' % (a, b)
    return s

def unicode_literals_python2():
    s = u'foo'
    return s

def invalid_escape_sequences_python2():
    s = '\d'
    return s

def is_is_not_comparison_python2(x):
    result = x is 5
    return result

def encode_to_bytes_literals_python2():
    s = 'foo'.encode()
    return s