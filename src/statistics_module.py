from scipy import stats
from numpy import std, mean, sqrt

def statistical_significance_ttest(samples1, samples2):
    return stats.ttest_ind(samples1, samples2)

def effect_size_cohensD(samples1, samples2):
    n_samples1 = len(samples1)
    n_samples2 = len(samples2)
    dof = n_samples1 + n_samples2 - 2
    return (mean(samples1) - mean(samples2)) / sqrt(((n_samples1 - 1) * std(samples1, ddof=1) ** 2 + (n_samples2 - 1) * std(samples2, ddof=1) ** 2) / dof)
