from mass_damper import find_acc, euler_step
import unittest
import numpy as np


class State(object):
    def __init__(self, x, v, m, k, c):
        self.x, self.v = x, v
        self.m, self.k, self.c = m, k, c


class Test_mass_damper(unittest.TestCase):
    def test_find_acc_function(self):
        st = State(3, 0, 1, 2.5, 2)
        self.assertAlmostEqual(find_acc(st.x, st.v, 1, 2.5, 2),
                               -7.5)
    def test_euler_step(self):
        st = State(3, 0, 1, 2.5, 2)
        np.testing.assert_array_almost_equal(euler_step(st.x, st.v,
                                                        st.m, st.k, st.c, 0.1), [3, -0.75] )

    def test_euler(self):
        pass
