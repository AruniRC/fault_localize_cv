import pandas as pd
import numpy as np
import statistics_module

def run_cv():
    df = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
    projects = np.unique(df["Project"])
    df['Family (Formula)'] = df['Family'] + "(" + df['Formula'] + ")"
    method_formula_pairs = np.unique(df['Family (Formula)'])
    fw = open("../results/cvnew.csv","w+")
    fw.write("Without_Project;Family (Formula);t_test;cohens_d\n")
    for project in projects:
        df_proj = df[df['Project'] != project]
        df_proj_real = df_proj[df_proj['isReal'] == 1]
        df_proj_artificial = df_proj[df_proj['isReal'] == 0]
        for method_formula_pair in method_formula_pairs:
            df_proj_real_type = df_proj_real[df_proj_real['Family (Formula)']==method_formula_pair]
            df_proj_artificial_type = df_proj_artificial[df_proj_artificial['Family (Formula)'] == method_formula_pair]
            samples_real = list(df_proj_real_type['ScoreWRTLoadedClasses'])
            samples_artificial = list(df_proj_artificial_type['ScoreWRTLoadedClasses'])
            t_test = statistics_module.statistical_significance_ttest(samples_real,samples_artificial)
            cohens_d = statistics_module.effect_size_cohensD(samples_real,samples_artificial)
            fw.write(project+";"+method_formula_pair+";"+str(t_test)+";"+str(cohens_d)+"\n")
    fw.close()

if __name__ == '__main__':
    run_cv()