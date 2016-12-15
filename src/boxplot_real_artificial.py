import seaborn as sns
import numpy as np
import pandas as pd
import pylab as plt
import matplotlib.patches as patches

#Set style
sns.set_style("whitegrid")
palette_col = sns.color_palette("Set2", 10)

#settings
x_col="Method"
y_col="Exam_Score"
hue_col = "Bug Type"
hue_order_col = ["Real","Artificial"]

#read data
data = pd.read_csv("../data/scores_artificial_vs_real_with_indicator.csv")
data[x_col] = data['Family'] + " " + data['Formula']
data[y_col] = data['ScoreWRTLoadedClasses']
data[hue_col] = ""
data[hue_col][data['isReal']==1] = hue_order_col[0]
data[hue_col][data['isReal']==0] = hue_order_col[1]
data = data[[x_col,y_col,hue_col]]
data.to_csv("../results/scores_artificial_vs_real.csv", index=None)

#Plot
ax = sns.violinplot(x=x_col, y=y_col, data=data, hue=hue_col, whis=np.inf, palette=palette_col, hue_order=hue_order_col )
ax = sns.stripplot(x=x_col, y=y_col, data=data,jitter=True, hue=hue_col,palette=palette_col, split=True, hue_order=hue_order_col )
ax.legend().set_visible(False)
ax.add_patch( patches.Rectangle(
        (0, (np.max(data[y_col]) - np.min(data[y_col]))*1.15),   # (x,y)
        0.5,          # width
        (np.max(data[y_col]) - np.min(data[y_col])) / 20,          # height
        color = '#66c2a5',
    ))
ax.add_patch(patches.Rectangle(
    (len(np.unique(data[x_col]))/2, (np.max(data[y_col]) - np.min(data[y_col]))*1.15),  # (x,y)
    0.5,  # width
    (np.max(data[y_col]) - np.min(data[y_col]))/20,  # height
    color='#fa8e63',
))

ax.text(0.6, (np.max(data[y_col]) - np.min(data[y_col]))*1.18, hue_order_col[0],
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=12)

ax.text(0.6+len(np.unique(data[x_col]))/2, (np.max(data[y_col]) - np.min(data[y_col]))*1.18, hue_order_col[1],
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=12)
#plt.ylim([0,1])
#plt.show()
plt.savefig("../visualizations/boxplot_real_artificial.pdf")