import numpy as np
import pandas as pd
from scipy import stats
import pycr

def pcr_efficiency(df, amount, reference_gene):
    dct = pycr.pcr_normalize(df, reference_gene)
    trend = pycr.pcr_trend(dct, amount)

    return trend

def pcr_standard(df, amount):
    trend = pycr.pcr_trend(df, amount)
    return trend
