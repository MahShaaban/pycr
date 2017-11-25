import numpy as np
import pandas as pd
import pycr

def pcr_ddct(df, group, reference_gene, reference_group, mode='separate_tube'):
    # calculate delta ct
    if mode == 'separate_tube':
        # average
        ave = pycr.pcr_average(df, group)
        dct = pycr.pcr_normalize(ave, reference_gene)

        # error
        sds = pycr.pcr_sd(df, group)
        error = pycr.pcr_error(sds, reference_gene)
    elif mode == 'same_tube':
        # average
        norm = pycr.pcr_normalize(df, reference_gene)
        dct = pycr.pcr_average(norm, group)

        # error
        error = pycr.pcr_sd(norm, group)

    else:
        print('User should provide a valid mode: separate_tube or same_tube')

    # claculate delta delta ct
    ddct = pycr.pcr_calibrate(dct, reference_group)


    # calculate relative expression
    norm_rel = ddct.applymap(lambda x: 2 ** (-x))

    # transform and merge
    ddct = ddct.unstack().reset_index()
    ddct.columns = ['gene', 'group', 'ddct']

    error = error.unstack().reset_index()
    error.columns = ['gene', 'group', 'error']

    norm_rel = norm_rel.unstack().reset_index()
    norm_rel.columns = ['gene', 'group', 'relative_expression']

    dat = ddct.merge(norm_rel).merge(error)

    # calculate intervals
    dat['lower'] = 2 ** (dat.ddct - dat.error)
    dat['upper'] = 2 ** (dat.ddct + dat.error)

    return dat

def pcr_dct(df, group, reference_group):
    # average dct
    ave = pycr.pcr_average(df, group)
    dct = pycr.pcr_calibrate(ave, reference_group)

    # error
    error = pycr.pcr_sd(df, group)

    # transform
    dct = dct.unstack().reset_index()
    dct.columns = ['gene', 'group', 'dct']

    error = error.unstack().reset_index()
    error.columns = ['gene', 'group', 'error']

    # calculate fold change
    dct['fold_change'] = 2 ** (- dct.dct)

    # merge
    dat = dct.merge(error)

    # calculate intervals
    dat['lower'] = 2 ** -(dat.dct + dat.error)
    dat['upper'] = 2 ** - (dat.dct - dat.error)

    return dat

def pcr_curve(df, group, reference_gene, reference_group, slope, intercept,
    mode='separate_tube'):
    amounts = pycr.pcr_amount(df, slope, intercept)

    if mode == 'separate_tube':
        # average
        ave = pycr.pcr_average(amounts, group)
        norm = pycr.pcr_normalize(ave, reference_gene, mode='divide')

        # error
        cv = pycr.pcr_cv(amounts, group)
        error = pycr.pcr_error(cv, reference_gene)
    elif mode == 'same_tube':
        # average
        norm = pycr.pcr_normalize(amounts, reference_gene, mode='divide')
        norm = pycr.pcr_average(norm, group)

        # error
        norm = pycr.pcr_normalize(amounts, reference_gene, mode='divide')
        error = pycr.pcr_cv(norm, group)
    else:
        print('Provide mode')

    calib = pycr.pcr_calibrate(norm, reference_group, 'divide')

    norm = norm.unstack().reset_index()
    norm.columns = ['gene', 'group', 'normalized_exp']

    calib = calib.unstack().reset_index()
    calib.columns = ['gene', 'group', 'calibrated_exp']

    error = error.unstack().reset_index()
    error.columns = ['gene', 'group', 'error']


    dat = pd.merge(calib, norm).merge(error)
    dat['lower'] = dat.calibrated_exp - dat.error
    dat['upper'] = dat.calibrated_exp * dat.error
    dat['error'] = dat.error * dat.normalized_exp

    return dat
