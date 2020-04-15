import numpy as np
import pandas as pd

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

print(s.str.lower())

print(s.str.upper())

print(s.str.len())

idx = pd.Index([' jack', 'jill ', ' jesse ', 'frank'])
idx2= pd.Index([' Tack', 'Till ', ' Tesse ', 'Trank'])

print("remove whitespace")
print(idx.str.strip())

print("left remove whitespace")
print(idx.str.lstrip())

print("reverse direction(right) remove whitespace")
print(idx.str.rstrip())


print(" ")
df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '], index=range(3))
print (df)

print(df.columns.str.strip())
print(df.columns.str.lower())
print(" ")

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df)