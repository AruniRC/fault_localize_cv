import pandas as pd
import seaborn as sns
import pylab as plt

def massage_data():
    df = pd.read_csv("../data/categories.csv")
    df['Error Type'] = ""
    df['Error Type'][df['Category']==1] = "Single Line"
    df['Error Type'][df['Category'] == 2] = "Omission"
    df['Error Type'][df['Category'] == 3] = "Non-executable"
    df['Project Name'] = df['PID']
    return df

def plotter_data(df):
    sns.set(style="white")
    palette_col = sns.color_palette("Set2", 10)
    sns.factorplot("Error Type", col="Project Name", col_wrap=5,data = df,kind = "count", palette=palette_col, size = 4, aspect = .8)
    plt.tight_layout()
    plt.savefig("../visualizations/bug_category.pdf")

if __name__ == '__main__':
    df = massage_data()
    plotter_data(df)