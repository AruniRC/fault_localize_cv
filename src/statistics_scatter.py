import seaborn as sns
import pylab as plt
import pandas as pd

def scatter_plot_p_value(file, type):
    plt.clf()
    data = pd.read_csv("../results/"+file,sep=";")
    sns.set_style("white")
    ax = sns.stripplot(x="Family (Formula)", y="t_test_p_value", hue=type+"_Project",data=data, jitter=True)
    plt.axhline(y=.05, color='k', ls='dashed')
    plt.legend(ncol=5, title=type+"_Project", loc="upper center")
    plt.savefig("../visualizations/p_value_"+file.split(".")[0]+".pdf")

def scatter_plot_cohen_d(file, type):
    plt.clf()
    data = pd.read_csv("../results/"+file,sep=";")
    sns.set_style("white")
    ax = sns.stripplot(x="Family (Formula)", y="cohens_d", hue=type+"_Project",data=data, jitter=True)
    plt.legend(ncol=5, title=type+"_Project", loc="upper center")
    plt.savefig("../visualizations/cohens_d_"+file.split(".")[0]+".pdf")

if __name__ == '__main__':
    file = "cvnew.csv"; type = "Without"
    scatter_plot_p_value(file, type)
    scatter_plot_cohen_d(file, type)

    file = "cvnew_ind.csv"; type = "With"
    scatter_plot_p_value(file, type)
    scatter_plot_cohen_d(file, type)