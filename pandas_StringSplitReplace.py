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