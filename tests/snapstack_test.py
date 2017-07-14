import unittest

from snapstack import Plan, Setup, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        # Setup override in base.Setup for locally built keystone.
        setup = Setup()
        setup.add_steps(('keystone', Step(
            snap='keystone',
            script_loc='./tests/',
            scripts=['keystone.sh'],
            snap_store=False)))

        # Execute the snapstack tests
        plan = Plan(base_setup=setup.steps())        
        plan.run()
