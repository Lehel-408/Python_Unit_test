import unittest
import functions
class TestAdatokFunction(unittest.TestCase):
    def test_add_five(self):
        self.assertEqual(functions.add_five(5), 10)

    def test_squared(self):
        self.assertEqual(functions.squared(5), 25)

    def test_add(self):
        self.assertEqual(functions.add(5, 5), 10)

    def test_to_upper(self):
        self.assertEqual(functions.to_upper("test"), "TEST")

    def test_concat(self):
        self.assertEqual(functions.concat("Hello, ", "world!"), "Hello, world!")

    def test_str_contains(self):
        self.assertEqual(functions.str_contains("Apple", "App"), True)

    def test_list_sum(self):
        self.assertEqual(functions.list_sum([1.5, 2.5, 3.0]), 7.0)
        self.assertEqual(functions.list_sum([]), 0.0)

    def test_count_fours(self):
        self.assertEqual(functions.count_fours([1, 4, 2, 4, 3]), 2)
        self.assertEqual(functions.count_fours([1, 2, 3]), 0)

    def test_list_add_five(self):
        self.assertEqual(functions.list_add_five([0, 5, -5]), [5, 10, 0])
        self.assertEqual(functions.list_add_five([]), [])

    def test_get_second(self):
        self.assertEqual(functions.get_second([10, 20, 30]), 20)

    def test_swap_elements(self):
        self.assertEqual(functions.swap_elements([1, 2]), [2, 1])

    def test_list_contains(self):
        self.assertEqual(functions.list_contains([1, 2, 3], 2), True)
        self.assertEqual(functions.list_contains([1, 2, 3], 5), False)

    def test_split_by(self):
        self.assertEqual(functions.split_by("alma,körte,szilva", ","), ["alma", "körte", "szilva"])

    def test_parse_numbers(self):
        self.assertEqual(functions.parse_numbers("1;2;3", ";"), [1, 2, 3])

    def test_parse_rows(self):
        self.assertEqual(functions.parse_rows("1,2\n3,4", ","), [[1, 2], [3, 4]])

    def test_calc_avgs(self):
        self.assertEqual(functions.calc_avgs([[1, 2, 3], [4, 6]]), [2.0, 5.0])