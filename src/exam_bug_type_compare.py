import seaborn as sns
import numpy as np
import pandas as pd
import pylab as plt

def get_Data():
    # Set style
    sns.set_style("white")
    palette_col = sns.color_palette("Set2", 10)

    # settings
    x_col = "Family (Formula)"
    y_col = "Exam_Score"
    hue_col = "Bug Type"
    hue_order_col = ["Real", "Artificial"]

    # read data
    data = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
    data[x_col] = data['Family'] + " (" + data['Formula'] + ")"
    data[y_col] = data['ScoreWRTLoadedClasses']
    data[hue_col] = ""
    data[hue_col][data['isReal'] == 1] = hue_order_col[0]
    data[hue_col][data['isReal'] == 0] = hue_order_col[1]
    data = data[[x_col, y_col, hue_col, "Project"]]
    return data

def plotter_kde(df):
    for project in np.unique(df["Project"]):
        df_Sel = df[df['Project']==project]
        df_Sel_real = df_Sel[df_Sel["Bug Type"]=="Real"]
        df_Sel_artificial = df_Sel[df_Sel["Bug Type"] == "Artificial"]
        plt.hist([df_Sel_real['Exam_Score'],df_Sel_artificial['Exam_Score']],stacked=True)
        #plt.show()
        plt.xlim([0,1])
        plt.savefig("../visualizations/real_artificial_histogram_"+project+".pdf")
        plt.clf()

if __name__ == '__main__':
    df = get_Data()
    plotter_kde(df)