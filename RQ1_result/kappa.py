import numpy as np
import pandas as pd
from scipy.stats import norm
from copy import deepcopy
from collections import Counter

repo_names = ["mindspore", 'pytorch', "tensorflow"]


def fleiss_kappa(data: np.array):
    """
    Calculates Fleiss' kappa coefficient for inter-rater agreement.
    Args:
        data: numpy array of shape (subjects, categories), where each element represents
              the number of raters who assigned a particular category to a subject.
    Returns:
        kappa: Fleiss' kappa coefficient.
    """
    subjects, categories = data.shape
    n_rater = np.sum(data[0])
    print(subjects, categories, n_rater)

    p_j = np.sum(data, axis=0) / (n_rater * subjects)
    P_e_bar = np.sum(p_j ** 2)

    P_i = (np.sum(data ** 2, axis=1) - n_rater) / (n_rater * (n_rater - 1))
    P_bar = np.mean(P_i)

    K = (P_bar - P_e_bar) / (1 - P_e_bar)

    tmp = (1 - P_e_bar) ** 2
    var = 2 * (tmp - np.sum(p_j * (1 - p_j) * (1 - 2 * p_j))) / (tmp * subjects * n_rater * (n_rater - 1))

    # standard error
    SE = np.sqrt(var)

    Z = K / SE

    p_value = 2 * (1 - norm.cdf(np.abs(Z)))

    ci_bound = 1.96 * SE / subjects
    print(f"ci_bound: {ci_bound}")
    lower_ci_bound = K - ci_bound
    upper_ci_bound = K + ci_bound

    print("Fleiss Kappa: {:.3f}".format(K))
    print("Standard Error: {:.3f}".format(SE))
    print("Z: {:.3f}".format(Z))
    print("p-value: {:.3f}".format(p_value))
    print("Lower 95% CI Bound: {:.3f}".format(lower_ci_bound))
    print("Upper 95% CI Bound: {:.3f}".format(upper_ci_bound))
    print()


alldata = pd.DataFrame(columns=(['URL', 'volunteer_1', 'volunteer_2', 'volunteer_3', 'volunteer_4',
                                 'volunteer_5', 'volunteer_6', 'Final_label']))


final_labels = []
for repo_name in repo_names:
    file_path = f'./{repo_name}.csv'
    data = pd.read_csv(file_path)

    alldata = alldata.append(deepcopy(data), ignore_index=True)

    kappa_data_csv = data.iloc[:, range(1, 1 + 6)]
    kappa_data = np.array(kappa_data_csv.apply(lambda row: pd.Series(row).value_counts(), axis=1).fillna(0))
    fleiss_kappa(kappa_data)

alldata_csv = alldata.iloc[:, range(1, 1 + 6)]
kappa_alldata = np.array(alldata_csv.apply(lambda row: pd.Series(row).value_counts(), axis=1).fillna(0))
fleiss_kappa(kappa_alldata)


















