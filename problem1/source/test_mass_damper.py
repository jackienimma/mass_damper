import unittest
from mass_damper import mass_spring_damp_acc


class TestMassDamper(unittest.TestCase):

    def test_mass_spring_damp_acc_normal(self):
        """Takes different positions and velocities, and compares
        the direction of acceleration with acceleration function.

        Note: From tests I found that with very high velocity
        this principle fails. DONT TAKE HIGH VELOCITIES.

        """
        for i in range(-3000, 3000):
            for j in range(-10, 10):
                # pos, vel = [random.randint(-i, i), random.randint(-i, i)]
                pos, vel = i, j
                [vel, acc] = mass_spring_damp_acc([pos, vel], 2)
                if pos > 0 and vel > 0:
                    assert acc < 0
                elif pos > 0 and vel <= 0:
                    assert acc < 0
                elif pos < 0 and vel > 0:
                    assert acc > 0
                elif pos == 0 and vel == 0:
                    assert acc == 0
                elif pos == 0 and vel > 0:
                    assert acc < 0
                elif pos == 0 and vel < 0:
                    assert acc > 0
                else:
                    assert acc > 0

unittest.main()
