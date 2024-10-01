import unittest

class TestStringManipulation(unittest.TestCase):

    def test_string_transformation(self):
        string = ' I like administration of hospital   '
        exclamation_point = '!'
        exclamation_point *= 3

        string = string.strip()
        string = string[:12].upper()

        expected_string = "I LIKE ADMINISTRAT".upper()
        self.assertEqual(string, expected_string)
        self.assertEqual(exclamation_point, "!!!")

    def test_short_string(self):
        string = 'Short string'
        exclamation_point = '!'
        exclamation_point *= 3

        string = string.strip()
        string = string[:12].upper()

        expected_string = "SHORT STRING".upper()
        self.assertEqual(string, expected_string)
        self.assertEqual(exclamation_point, "!!!")

    def test_empty_string(self):
        string = ''
        exclamation_point = '!'
        exclamation_point *= 3

        string = string.strip()
        string = string[:12].upper()

        expected_string = ''
        self.assertEqual(string, expected_string)
        self.assertEqual(exclamation_point, "!!!")

if __name__ == '__main__':
    unittest.main()
