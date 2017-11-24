from unittest import TestCase

import pycr
import numpy as np
import pandas as pd

ct1 = pd.read_csv('pycr/ct1.csv')
group = np.repeat(['brain', 'kidney'], 6)

class TestMock(TestCase):
    def test_is_string(self):
        s = pycr.mock()
        self.assertTrue(isinstance(s, str))
