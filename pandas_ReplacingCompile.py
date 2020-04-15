import numpy as np
import pandas as pd
import re
"""
re.compile(pattern, repl, string):
 We can combine a regular expression pattern into pattern objects, 
 which can be used for pattern matching.
 It also helps to search a pattern again without rewriting it.
"""

s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca','', np.nan, 'CABA', 'dog', 'cat'], dtype=str)
regex_pat = re.compile(r'^.a|dog', flags=re.IGNORECASE)
print(s3.str.replace(regex_pat, 'XX-XX '))
print("________________")
"""
Including a flags argument when calling replace with a compiled regular
expression object will raise a ValueError.
In [55]: s3.str.replace(regex_pat, 'XX-XX ', flags=re.IGNORECASE)
---------------------------------------------------------------------------
ValueError: case and flags cannot be set when pat is a compiled regex
Concatenation¶
"""

pattern=re.compile('TP')
result=pattern.findall('TP Tutorialspoint TP')
print(result)
print("_______________________________")
result2=pattern.findall('TP is most popular tutorials site of India')
print(result2)