from unittest import TestCase

import numpy as np
import pandas as pd
import pycr
from scipy import stats


class test_pcr_ttest(TestCase):
    def test_pcr_ttest(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        d = pycr.pcr_ttest(ct1, group, 'GAPDH', 'brain')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (1, 3))

class test_pcr_wilcoxon(TestCase):
    def test_pcr_wilcoxon(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        d = pycr.pcr_wilcoxon(ct1, group, 'GAPDH', 'brain')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (1, 3))
