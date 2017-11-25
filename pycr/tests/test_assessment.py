from unittest import TestCase

import pycr
import numpy as np
import pandas as pd

class test_pcr_efficiency(TestCase):
    def test_pcr_efficiency(self):
        ct3 = pd.read_csv('pycr/ct3.csv')
        amount = np.array([1, .5, .2, .1, .05, .02, .01]).repeat(3)

        d = pycr.pcr_efficiency(ct3, amount, 'GAPDH')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (1, 6))

class test_pcr_standard(TestCase):
    def test_pcr_standard(self):
        ct3 = pd.read_csv('pycr/ct3.csv')
        amount = np.array([1, .5, .2, .1, .05, .02, .01]).repeat(3)
        d = pycr.pcr_standard(ct3, amount)
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (2, 6))
