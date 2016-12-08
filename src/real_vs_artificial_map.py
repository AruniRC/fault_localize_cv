import pandas as pd
import numpy as np

def add_indicator():
    df = pd.read_csv("../data/scores_artificial_vs_real.csv")
    df['isReal'] = 0
    df['isReal'][df.Bug < 1000] = 1
    df['isReal'][df.Bug > 100000] = 0
    df.to_csv("../data/scores_artificial_vs_real_with_indicator.csv", index=None)

def create_map():
    df = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
    df_real = df[df['isReal']==1]
    real_bug_ids = list(np.unique(df_real['Bug']))
    d = {}
    for real_bug_id in real_bug_ids:
        df_sel_art = df[df['Bug']>=real_bug_id*100000]
        df_sel_art = df_sel_art[df_sel_art['Bug']<(real_bug_id+1)*100000]
        d[real_bug_id] = sorted(list(np.unique(df_sel_art['Bug'])))
    df_map = pd.DataFrame(d.items(), columns=['Real_Bug_ID', 'Artificial_Bug_IDs'])
    #Used excel as list has commas
    df_map.to_excel("../data/real_artificial_map.xlsx", index=None)

if __name__ == '__main__':
    add_indicator()
    create_map()
