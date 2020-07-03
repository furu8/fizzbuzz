"""
このファイルに解答コードを書いてください
"""
import pandas as pd

def read_text(path):
    df = pd.read_table(path, sep=':', names=['num', 'str'])
    return df

def main(df, m):
    df = df.dropna()
    df['num'] = df['num'].astype(int)
    df['rem'] = m % df['num']

    ans_df = df.loc[df['rem']==0]
    ans_df = ans_df.sort_values('num')
    
    ans = ''
    for s in ans_df['str'].values:
        ans += s

    if not ans:
        print(m)
    else:
        print(ans)

if __name__ == "__main__":
    path = 'input.txt'
    # path = 'sample1.txt'
    # path = 'sample2.txt'

    df = read_text(path)
    m = int(df['num'].tail(1))

    main(df, m)