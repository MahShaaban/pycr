from unittest import TestCase

import pycr
import numpy as np
import pandas as pd

from scipy import stats

class test_pcr_average(TestCase):
    def test_pcr_average(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        d = pycr.pcr_average(ct1, group)
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (2, 2))

class test_pcr_sd(TestCase):
    def test_pcr_sd(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        d = pycr.pcr_sd(ct1, group)
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (2, 2))

class test_pcr_error(TestCase):
    def test_pcr_error(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        s = pycr.pcr_sd(ct1, group)
        d = pycr.pcr_error(s, 'GAPDH')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (2, 2))

class test_pcr_normalize(TestCase):
    def test_pcr_normalize(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        d = pycr.pcr_normalize(ct1, 'GAPDH')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (12, 1))

        d = pycr.pcr_normalize(ct1, 'GAPDH', mode='divide')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (12, 1))

class test_pcr_calibrate(TestCase):
    def test_pcr_calibrate(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        a = pycr.pcr_average(ct1, group)
        n = pycr.pcr_normalize(a, 'GAPDH')
        d = pycr.pcr_calibrate(n, 'brain')
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (2, 1))

class test_pcr_trend(TestCase):
    def test_pcr_trend(self):
        ct3 = pd.read_csv('pycr/ct3.csv')
        amount = np.array([1, .5, .2, .1, .05, .02, .01]).repeat(3)
        d = pycr.pcr_trend(ct3, amount)
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (2, 6))

class test_pcr_amount(TestCase):
    def test_pcr_amount(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        ct3 = pd.read_csv('pycr/ct3.csv')
        amount = np.array([1, .5, .2, .1, .05, .02, .01]).repeat(3)
        slope = pycr.pcr_trend(ct3, amount)['slope']
        intercept = pycr.pcr_trend(ct3, amount)['intercept']

        d = pycr.pcr_amount(ct1, slope, intercept)
        self.assertIs(d.empty, False)
        self.assertEqual(d.shape, (12, 2))

class test_pcr_cv(TestCase):
    def test_pcr_cv(self):
        ct1 = pd.read_csv('pycr/ct1.csv')
        group = np.repeat(['brain', 'kidney'], 6)

        ct3 = pd.read_csv('pycr/ct3.csv')
        amount = np.array([1, .5, .2, .1, .05, .02, .01]).repeat(3)
        slope = pycr.pcr_trend(ct3, amount)['slope']
        intercept = pycr.pcr_trend(ct3, amount)['intercept']

        df = pycr.pcr_amount(ct1, slope, intercept)
        d = pycr.pcr_cv(df, group)
        self.assertIs(d.empty, False)
