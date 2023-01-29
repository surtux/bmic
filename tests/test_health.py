"""Python to test """
from unittest import TestCase
from bmic.src import health

class TestHealth(TestCase):
    """
    All the test for my imc function are written here
    """
    def test_imc(self):
        """
        Test the imc function with good and bad values.
        Essentially, i test to assure that any bad values
        is passed to the function. So to speak,
        str, null value and negative number should not be passed
        """
        response = health.imc(1.74, 77)
        self.assertEqual(response, 25.43268595587264)
        with self.assertRaises(ValueError):
            health.imc(-1.60, 56)
        with self.assertRaises(ValueError):
            health.imc(1.60, -56)
        with self.assertRaises(ZeroDivisionError):
            health.imc(0, 52)
        with self.assertRaises(ZeroDivisionError):
            health.imc(1.60, 0)
        with self.assertRaises(TypeError):
            health.imc('5"5', 70)
        with self.assertRaises(TypeError):
            health.imc(1.74, '40kg')
        with self.assertRaises(TypeError):
            health.imc('5"5', '40kg')
