import numpy as np
import pandas as pd
""" Some caution must be taken to keep regular expressions in mind! For example, 
the following code will cause trouble because of the regular expression meaning of $: 
# Consider the following badly formatted financial data """
dollars = pd.Series(['12', '-$10', '$10,000'], dtype= str)

"""# This does what you'd naively expect: """
print(dollars.str.replace('$', ''))

""" # But this doesn't:"""
print(dollars.str.replace('-$', '-'))

"""# We need to escape the special character (for >1 len patterns) """
print(dollars.str.replace(r'-\$', '-'))

"""
New in version 0.23.0.
If you do want literal replacement of a string (equivalent to str.replace()), 
you can set the optional regex parameter to False, rather than escaping each 
character. In this case both pat and repl must be strings:
    
# These lines are equivalent
             ^^^
"""
print(dollars.str.replace(r'-\$', '-'))

print(dollars.str.replace('-$', '-', regex=False))
print("_____________________________")
"""callable-ADJECTIVE-finance-designating a bond that can be paid off earlier than the maturity date."""
"""The replace method can also take a callable as replacement. It is called on every pat using re.sub(). 
The callable should expect one positional argument (a regex object) and return a string."""
""" # Reverse every lowercase alphabetic word """
pat = r'[a-z]+'
def repl(m):
    return m.group(0)[::-1]

print(pd.Series(['foo 123', 'bar baz', np.nan], dtype= str).str.replace(pat, repl))
""" # Using regex groups
A regular expression, regex or regexp (sometimes called a rational expression) is a sequence of 
characters that define a search pattern. Usually such patterns are used by string searching 
algorithms for "find" or "find and replace" operations on strings, or for input validation."""
print("________________________")

pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"
def repl(m):
        return m.group('two').swapcase()
print(pd.Series(['Foo Bar Baz', np.nan], dtype= str).str.replace(pat, repl))

