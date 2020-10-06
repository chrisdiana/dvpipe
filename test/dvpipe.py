import pandas as pd
from dvpipe import pipe


data = {'col1': [1, 2, 2], 'col2': [3, 4, 5], 'col3': [1, 2, 3]}
df = pd.DataFrame(data)


def clean(df):
    return df[['col1', 'col2']]


def equals_2(df, col):
    return df.loc[df[col] == 2]


df = (pipe(df,
    clean,
    (equals_2, 'col1')))

print(df)
