import seaborn as sns
import pylab as plt
import pandas as pd
import matplotlib.patches as mpatches

def scatter_plot_mean_score():
    plt.clf()
    data = pd.read_csv("../results/cv_mean_score.csv",sep=";")
    sns.set_style("white")
    ax = sns.stripplot(x="Family (Formula)", y="MeanScoreReal", data=data, jitter=True, color="seagreen")
    ax = sns.stripplot(x="Family (Formula)", y="MeanScoreArt", data=data, jitter=True, color="black")
    real_patch = mpatches.Patch(color="seagreen", label="Real Faults")
    art_patch = mpatches.Patch(color="black", label="Artificial Faults")
    plt.legend(handles=[real_patch, art_patch])
    ax.set(xlabel="Family (Formula)", ylabel="Mean EXAM Score")
    plt.savefig("../visualizations/mean_scores.pdf")

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

    