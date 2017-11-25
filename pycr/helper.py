import numpy as np
import pandas as pd
from scipy import stats

def pcr_average(df, group):
    ave = df.groupby(group).mean()
    return ave

def pcr_sd(df, group):
    sd = df.groupby(group).std()
    return sd

def pcr_error(df, reference_gene):
    error = df.apply(lambda x: np.sqrt(x ** 2 + df[reference_gene] ** 2))
    return error

def pcr_normalize(df, reference_gene, mode='subtract'):
    if mode == 'subtract':
        norm = df.apply(lambda x: x - df[reference_gene])
    elif mode == 'divide':
        norm = df.apply(lambda x: x / df[reference_gene])
    else:
        print('User should provide a valid mode: subtract or divide')

    norm = norm.drop(reference_gene, axis=1)
    return norm

def pcr_calibrate(df, reference_group, mode = 'subtract'):
    if mode == 'subtract':
        calib = df.apply(lambda x: x - df.loc[reference_group],axis=1)
    elif mode == 'divide':
        calib = df.apply(lambda x: x / df.loc[reference_group],axis=1)
    else:
        print('User should provide a valid mode: subtract or divide')

    return calib

def pcr_trend(df, amount):
    lm = df.apply(lambda x: stats.linregress(np.log10(amount),x))
    lm = pd.DataFrame(lm)
    lm = lm.apply(lambda x: x.apply(pd.Series).stack()).unstack().reset_index()
    lm.columns = ['gene', 'slope', 'intercept', 'r_value', 'p_value', 'std']
    return lm

def pcr_amount(df, slope, intercept):
    ind = df.columns
    df.columns = [0, 1]
    dat = df.apply(lambda x: 10 ** ((x - intercept[x.index])/slope[x.index]), axis=1)
    dat.columns = ind
    return dat

def pcr_cv(df, group):
    ave = df.groupby(group).mean()
    sds = df.groupby(group).std()
    cv = ave / sds

    return cv
