import seaborn as sns
import pylab as plt
import pandas as pd

def scatter_plot():
    data = pd.read_csv("../results/cvnew.csv",sep=";")
    sns.set_style("whitegrid")
    ax = sns.stripplot(x="Family (Formula)", y="t_test_p_value", data=data, jitter=True)
    plt.savefig("../visualizations/p_value.pdf")

if __name__ == '__main__':
    scatter_plot()