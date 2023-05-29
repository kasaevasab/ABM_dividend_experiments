import numpy as np
from scipy.stats import kruskal
from scikit_posthocs import posthoc_dunn
import typing as tp
import pandas as pd


def kruskal_wallis_test(test_data: tp.List[list]):
    statistic, p_value = kruskal(*test_data)
    # print("Kruskal-Wallis test statistic:", statistic)
    # print("p-value:", p_value)
    return p_value


# def dunn_test(test_data: tp.List[list], labels: tp.List[str]):
#     all_data = np.concatenate(test_data)
#     group_labels = np.repeat(labels, [len(sample) for sample in test_data])
#     dunn_results = posthoc_dunn(all_data, group_labels, p_adjust='bonferroni')
#     # print(dunn_results)
#     return dunn_results


def dunn_test(samples: tp.List[list], labels: tp.List[str]):
    data_array = np.array(samples)
    stat, p = kruskal(*data_array.T)
    print(p)
    if p < 1:
        data = pd.DataFrame({'Group': np.repeat(labels, [len(s) for s in samples]),
                             'Value': np.concatenate(samples)})
        print(data)
        dunn_results = posthoc_dunn(data, group_col='Group', val_col='Value', p_adjust='bonferroni')
        return dunn_results
    else:
        print("No significant differences between the groups.")
        return None
