import numpy as np
import pandas as pd

"""Methods like split return a Series of lists: """
s2 = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'], dtype=str)

print(s2.str.split('_'))

"""Elements in the split lists can be accessed using get or [] notation:"""

print(s2.str.split('_').str.get(1))

print(s2.str.split('_').str[1])

""" It is easy to expand this to return a DataFrame using expand."""
print(s2.str.split('_', expand=True))

""" When original Series has StringDtype, the output columns will all be StringDtype as well.
It is also possible to limit the number of splits:"""

print(s2.str.split('_', expand=True, n=1))

"""rsplit is similar to split except it works in the reverse direction, i.e., from the end of the string to the beginning of the string: """

""" rsplit is similar to split except it works in the reverse direction, i.e., from the end of the string to the beginning of the string: """

print(s2.str.rsplit('_', expand=True, n=1))




