import unittest
import numpy as np
import random
from hypothesis import given, example
from hypothesis import strategies as st
from mass_damper import mass_spring_damp_acc


class TestMassDamper(unittest.TestCase):
    """Test for a3 functions"""

    # @given(x=st.integers(), y=st.integers())
    # def test_mass_spring_damp_acc(self, x, y):
    #     [vel, acc] = mass_spring_damp_acc([x, y], 2)
    #     if x > 0 and y > 0:
    #         assert acc < 0
    #     elif x > 0 and y <= 0:
    #         assert acc < 0
    #     elif x < 0 and y > 0:
    #         assert acc > 0
    # elif x == 0 and y == 0:
    #     assert acc == 0
    # else:
    #     assert acc > 0

    def test_mass_spring_damp_acc_normal(self):
        for i in range(1, 100):
            # pos, vel = [random.randint(-i, i), random.randint(-i, i)]
            [vel, acc] = mass_spring_damp_acc([pos, vel], 2)
            if pos > 0 and vel > 0:
                assert acc < 0
            elif pos > 0 and vel <= 0:
                assert acc > 0
            elif pos < 0 and vel > 0:
                assert acc > 0
            elif pos == 0 and vel == 0:
                assert acc == 0
            else:
                assert acc > 0
