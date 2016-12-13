import pandas as pd
import numpy as np
import statistics_module

def run_cv_scores():
    df = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
    projects = np.unique(df["Project"])
    df['Family (Formula)'] = df['Family'] + "(" + df['Formula'] + ")"
    method_formula_pairs = np.unique(df['Family (Formula)'])
    fw = open("../results/cv_mean_score.csv","w+")
    fw.write("Without_Project;Family (Formula);MeanScoreReal;MeanScoreArt;CountReal;CountArt\n")
    for project in projects:
        df_proj = df[df['Project'] != project]
        df_proj_real = df_proj[df_proj['isReal'] == 1]
        df_proj_artificial = df_proj[df_proj['isReal'] == 0]
        for method_formula_pair in method_formula_pairs:
            df_proj_real_type = df_proj_real[df_proj_real['Family (Formula)']==method_formula_pair]
            df_proj_artificial_type = df_proj_artificial[df_proj_artificial['Family (Formula)'] == method_formula_pair]
            samples_real = list(df_proj_real_type['ScoreWRTLoadedClasses'])
            samples_artificial = list(df_proj_artificial_type['ScoreWRTLoadedClasses'])
            mean_score_real = np.array(samples_real).mean()
            mean_score_art = np.array(samples_artificial).mean()
            count_real = len(samples_real)
            count_art = len(samples_artificial)
            fw.write(project+";"+method_formula_pair+";"+str(mean_score_real)+";"+str(mean_score_art)+";"+str(count_real)+";"+str(count_art)+"\n")
    fw.close()


if __name__ == '__main__':
	run_cv_scores()


