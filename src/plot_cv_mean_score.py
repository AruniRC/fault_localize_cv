import seaborn as sns
import pylab as plt
import pandas as pd
import matplotlib.patches as mpatches
import numpy as np

def scatter_plot_mean_score():
    plt.clf()
    data = pd.read_csv("../results/cv_mean_score.csv",sep=";", index_col=None)
    sns.set_style("white")
    ax = sns.stripplot(x="Family (Formula)", y="MeanScoreReal", data=data, jitter=True, color="seagreen")
    ax = sns.stripplot(x="Family (Formula)", y="MeanScoreArt", data=data, jitter=True, color="black")
    real_patch = mpatches.Patch(color="seagreen", label="Real Faults")
    art_patch = mpatches.Patch(color="black", label="Artificial Faults")
    plt.legend(handles=[real_patch, art_patch])
    ax.set(xlabel="Family (Formula)", ylabel="Mean EXAM Score")
    plt.savefig("../visualizations/mean_scores.pdf")

    sLength = len(data['MeanScoreReal'])
    data['MeanScoreDiff'] = pd.Series(np.random.randn(sLength), index=data.index)
    data[['MeanScoreDiff', 'MeanScoreReal']].sub(data['MeanScoreArt'], axis=0)
    data['MeanScoreDiff'] = data['MeanScoreReal'] - data['MeanScoreArt']
    data = data[['Without_Project','Family (Formula)','MeanScoreDiff']]
    data = data.groupby(['Without_Project','Family (Formula)']).mean()
    data = data.unstack()
    axes = plt.figure(figsize=(10, 6)).add_subplot(111)
    sns.heatmap(data)
    plt.xticks([t+0.5 for t in range(len(axes.get_xticklabels()))],[val.get_text().replace("MeanScoreDiff-","") for val in axes.get_xticklabels()])
    plt.ylabel("Without_Project",fontsize=14)
    plt.xlabel("Difference between the mean exam scores for real and artificial bugs", fontsize=14)
    plt.tight_layout()
    plt.savefig("../visualizations/difference_real_artificial.pdf")

def bar_plot_count_real():
    plt.clf()
    data = pd.read_csv("../results/cv_mean_score.csv",sep=";")
    ax = sns.set_style("white")
    ax = sns.barplot(x="Without_Project", y="CountReal", data=data)
    ax.set(xlabel="Fold(Without_project)", ylabel="Count_Real")
    plt.savefig("../visualizations/cv_counts_real.pdf")
    

def bar_plot_count_artificial():
    plt.clf()
    data = pd.read_csv("../results/cv_mean_score.csv",sep=";")
    ax = sns.set_style("white")
    ax = sns.barplot(x="Without_Project", y="CountArt", data=data)
    ax.set(xlabel="Fold(Without_project)", ylabel="Count_Artificial")
    plt.savefig("../visualizations/cv_counts_artificial.pdf")
    

if __name__ == '__main__':
    scatter_plot_mean_score()
    bar_plot_count_real()
    bar_plot_count_artificial()

    