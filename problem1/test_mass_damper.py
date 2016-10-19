import unittest
import numpy as np
from hypothesis import given, example
from hypothesis import strategies as st
from mass_damper import mass_spring_damp_acc


class TestMassDamper(unittest.TestCase):
    """Test for a3 functions"""

    # @given(x = st.integers(), y = st.integers())
    def test_mass_spring_damp_acc(self, x, y):
        [vel, acc] = mass_spring_damp_acc([x, y], 2)
        if x > 0 and y > 0:
            assert acc >= 0
        elif x > 0 and y <= 0:
            assert acc < 0
        elif x < 0 and y > 0:
            assert acc > 0
        else:
            assert acc < 0

    def test_mass_spring_damp_acc_normal(self):
        pos, vel = [-3, -3]
        [vel, acc] = mass_spring_damp_acc([pos, vel], 2)
        if pos > 0 and vel > 0:
            assert acc >= 0
        elif pos > 0 and vel <= 0:
            assert acc < 0

    @given(st.integers(), st.integers())
    def func_linear(self, x, y):
        print(x, y)
        assert x + y == y + x

    def func_quad(self, x):
        return x**2
