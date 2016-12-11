import seaborn as sns
import pylab as plt
import pandas as pd

def scatter_plot_p_value():
    data = pd.read_csv("../results/cvnew.csv",sep=";")
    sns.set_style("white")
    ax = sns.stripplot(x="Family (Formula)", y="t_test_p_value", hue="Without_Project",data=data, jitter=True)
    plt.axhline(y=.05, color='k', ls='dashed')
    plt.legend(ncol=5, title="Without_Project", loc="upper center")
    plt.savefig("../visualizations/p_value.pdf")

def scatter_plot_cohen_d():
    plt.clf()
    data = pd.read_csv("../results/cvnew.csv",sep=";")
    sns.set_style("white")
    ax = sns.stripplot(x="Family (Formula)", y="cohens_d", hue="Without_Project",data=data, jitter=True)
    plt.legend(ncol=5, title="Without_Project", loc="upper center")
    plt.savefig("../visualizations/cohens_d.pdf")

if __name__ == '__main__':
    scatter_plot_p_value()
    scatter_plot_cohen_d()