import numpy as np
import pandas as pd
import pycr
from scipy import stats

def pcr_ttest(df, group, reference_gene, reference_group):
    norm  = pycr.pcr_normalize(df, reference_gene)
    ind = group == reference_group

    tst = norm.apply(lambda x: stats.ttest_ind(x[ind], x[~ind]))
    tst = pd.DataFrame(tst)
    tst = tst.apply(lambda x: x.apply(pd.Series).stack()).unstack().reset_index()
    tst.columns = ['gene', 'statistics', 'p_value']
    return tst

def pcr_wilcoxon(df, group, reference_gene, reference_group):
    norm  = pycr.pcr_normalize(df, reference_gene)
    ind = group == reference_group

    tst = norm.apply(lambda x: stats.wilcoxon(x[ind], x[~ind]))
    tst = pd.DataFrame(tst)
    tst = tst.apply(lambda x: x.apply(pd.Series).stack()).unstack().reset_index()
    tst.columns = ['gene', 'statistics', 'p_value']
    return tst
