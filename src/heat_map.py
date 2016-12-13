import pandas as pd
import seaborn as sns
import pylab as plt

#Project, Family+Formula,
def heatmap():
    df = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
    df['Family (Formula)'] = df['Family'] + "(" + df['Formula'] + ")"
    df = df[['Project','Family (Formula)','ScoreWRTLoadedClasses','isReal']]
    df_real = df[df['isReal']==1]
    df_artificial = df[df['isReal']==0]

    df_real_group = df_real.groupby(['Project','Family (Formula)']).mean()
    df_artificial_group = df_artificial.groupby(['Project','Family (Formula)']).mean()
    df_final = df_real_group[['isReal']]
    df_final['Difference'] = df_real_group.ScoreWRTLoadedClasses - df_artificial_group.ScoreWRTLoadedClasses
    df_final = df_final[['Difference']]
    data = df_final.unstack()
    return data

if __name__ == '__main__':
    data = heatmap()
    axes = plt.figure(figsize=(10, 6)).add_subplot(111)
    sns.heatmap(data)
    plt.xticks([t+0.5 for t in range(len(axes.get_xticklabels()))],[val.get_text().replace("Difference-","") for val in axes.get_xticklabels()])
    plt.ylabel("Project",fontsize=14)
    plt.xlabel("Difference between the exam scores for real and artificial bugs", fontsize=14)
    plt.tight_layout()
    plt.savefig("../visualizations/difference_real_artificial.pdf")