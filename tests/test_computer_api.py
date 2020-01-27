import unittest
import fetch

class TestComputerApi(unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_fetch_all(self):
        computers = fetch.all_computers()
        self.assertIn({'com_id': 1, 'name': 'Delora', 'price': 1430, 'ram': 13, 'disk': 460, 'quantity': 24}, computers)
        self.assertIn({'com_id': 2, 'name': 'Joni', 'price': 1072, 'ram': 16, 'disk': 496, 'quantity': 27}, computers)
        self.assertIn({'com_id': 3, 'name': 'Xena', 'price': 1253, 'ram': 15, 'disk': 252, 'quantity': 13}, computers)
        self.assertIn({'com_id': 4, 'name': 'Maible', 'price': 550, 'ram': 12, 'disk': 465, 'quantity': 10}, computers)

    def test_fetch_one(self):
        self.assertEqual({'com_id': 4, 'name': 'Maible', 'price': 550, 'ram': 12, 'disk': 465, 'quantity': 10}, fetch.one_computer(4))
        self.assertEqual({'com_id': 2, 'name': 'Joni', 'price': 1072, 'ram': 16, 'disk': 496, 'quantity': 27}, fetch.one_computer(2))

