import pandas as pd
import numpy as np

def run_cv():
    df = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
    projects = np.unique(df["Project"])
    df['Method (Formula)'] = df['Method'] + "(" + df['Formula'] + ")"
    method_formula_pairs = np.unique(df['Method (Formula)'])
    for project in projects:
        df_proj = df[df['Project'] != project]
        df_proj_real = df_proj[df_proj['isReal'] == 1]
        df_proj_artificial = df_proj[df_proj['isReal'] == 0]
        for method_formula_pair in method_formula_pairs:
            df_proj_real_type = df_proj_real[df_proj_real['Method (Formula)']==method_formula_pair]
            df_proj_artificial_type = df_proj_artificial[df_proj_artificial['Method (Formula)'] == method_formula_pair]
            samples_real = list(df_proj_real_type['ScoreWRTLoadedClasses'])
            samples_artificial = list(df_proj_artificial_type['ScoreWRTLoadedClasses'])


if __name__ == '__main__':
    run_cv()