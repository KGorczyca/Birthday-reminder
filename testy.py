import unittest
import os.path
import csv
import datetime

from uniwersary_program import Birthday


class BirthdayTest(unittest.TestCase):
    def setUp(self):
        self.person = Birthday('Katarzyna', 'Kowalska', '29.09.1986')

    def test_initialization(self):
        self.assertTrue(self.person)

    def test_add_to_date_of_birth_list(self):
        self.person.appending()
        self.assertEqual(self.person.date_of_birth, [['Katarzyna', 'Kowalska', '29.09.1986']] )


    def test_creating_file(self):
        self.person.create_file('test_file.csv')
        my_file = 'test_file.csv'
        self.assertTrue(os.path.exists(my_file))


    def test_writing_in_file(self):
        with open('test_file.csv', 'r') as f:
            reader = csv.reader(f)
            reader = list(reader)
            self.assertEqual(reader,[['Katarzyna', 'Kowalska', '29.09.1986']])



if __name__ == '__main__':
    unittest.main()