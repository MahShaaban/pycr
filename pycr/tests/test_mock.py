from unittest import TestCase

import pycr

class TestMock(TestCase):
    def test_is_string(self):
        s = pycr.mock()
        self.assertTrue(isinstance(s, str))
