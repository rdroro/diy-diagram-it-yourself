import unittest
from gridManagement import GridManagement

class TestGridManagement(unittest.TestCase):
	"""
	To run tests please setup PYTHONPATH as:
	export PYTHONPATH=path_to_project_folder/diy-diagram-it-yourself/bin:${PYTHONPATH}
	and run tests by typing following command:
	python -m unittest discover -s unit-test -p 'Test*'
	"""

	def setUp(self):
		print '== Test GridManagement =='

	def runTest(self):
		print 'Test GridManagement.getPosition(1, 1)'
		position = GridManagement.getPosition(1, 1)
		self.assertEqual(GridManagement.X_SIZE, position['x'])
		self.assertEqual(GridManagement.Y_SIZE, position['y'])

		print 'Test GridManagement.getPosition(2, 1)'
		position = GridManagement.getPosition(2, 1)
		self.assertEqual(GridManagement.X_SIZE*2, position['x'])
		self.assertEqual(GridManagement.Y_SIZE, position['y'])


if __name__ == '__main__':
    unittest.main()
