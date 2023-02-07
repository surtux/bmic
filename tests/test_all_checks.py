"""
This python file will implement all the checks regardind our programm
Mainly in th app.py.
"""
from unittest import TestCase
from bmic.src import checks

class TestChecks(TestCase):
    """
    The purpose of this class is to test the checks function that will be implemented
    in another python file
    """
    #################################################################################
    #                               TESTS FIXTURE                                   #
    #################################################################################





    #################################################################################
    #                                 TESTS                                         #
    #################################################################################

    def test_check_password(self):
        """
        This test will be implement in future with regex. For now we will test with
        values contain into a list of bad password. So the test should ensure that
        The user doesn't enter a password in this list. The next future improvements will be
        to use a password dictionnary for this purpose. If the password provided is good
        it should not be in the  list
        """
        bad_password = "1234"
        good_password = "Elisee 1e lionne"
        self.assertEqual(checks.check_password(bad_password),True)
        self.assertEqual(checks.check_password(good_password), False)