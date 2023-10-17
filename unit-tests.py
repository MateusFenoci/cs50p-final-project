import unittest
from project import remove_duplicates, distance_calculator, route_tracer, route

class TestProjectFunctions(unittest.TestCase):
    def test_remove_duplicates(self):
        cords = [(1.0, 2.0), (3.0, 4.0), (1.0, 2.0)]
        result = remove_duplicates(cords)
        self.assertEqual(result, [(1.0, 2.0), (3.0, 4.0)])

    def test_distance_calculator(self):
        x1 = (1.0, 2.0)
        x2 = (3.0, 4.0)
        result = distance_calculator(x1, x2)
        self.assertAlmostEqual(result, 2.8284271247461903, places=6)

    def test_route_tracer(self):
        first_point = (1.0, 2.0)
        cords = [(3.0, 4.0), (5.0, 6.0), (7.0, 8.0)]
        result = route_tracer(first_point, cords)
        self.assertEqual(result, (3.0, 4.0))

    def test_route(self):
        first_point = (1.0, 2.0)
        cords = [(3.0, 4.0), (5.0, 6.0), (7.0, 8.0)]
        result = route(first_point, cords)
        self.assertEqual(result, [(3.0, 4.0), (5.0, 6.0), (7.0, 8.0)])

if __name__ == '__main__':
    unittest.main()
