import numpy as np
import pandas as pd
""" replace by default replaces regular expressions: """
s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca','', np.nan, 'CABA', 'dog', 'cat'], dtype=str)
print(s3)

print(s3.str.replace('^.a|dog', 'XX-XX ', case=False))

