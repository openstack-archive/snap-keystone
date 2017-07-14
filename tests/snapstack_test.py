import unittest

from snapstack import Plan, Setup, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        setup = Setup()
        # Override keystone in base with locally build keystone.
        setup.add_steps(('keystone', Step(
            snap='keystone',
            script_loc='./tests/',
            scripts=['keystone.sh'],
            snap_store=False)))

        plan = Plan(base_setup=setup.steps())
        plan.run()
