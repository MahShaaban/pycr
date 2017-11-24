from unittest import TestCase

import pycr
import numpy as np
import pandas as pd


class test_pcr_ddct(TestCase):
    def test_is_string(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        d = pycr.pcr_ddct(ct1, group, 'GAPDH', 'brain')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (4, 7))

        d = pycr.pcr_ddct(ct1, group, 'GAPDH', 'brain', 'same_tube')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (4, 7))

class test_pcr_curve(TestCase):
    def test_pcr_curve(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        ct3 = pd.read_csv('pycr/ct3.csv')
        amount = np.array([1, .5, .2, .1, .05, .02, .01]).repeat(3)
        slope = pycr.pcr_trend(ct3, amount)['slope']
        intercept = pycr.pcr_trend(ct3, amount)['intercept']

        d = pycr.pcr_curve(ct1, group, 'GAPDH', 'brain', slope, intercept)
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (4, 7))
