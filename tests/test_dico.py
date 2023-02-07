"""
The purpose of this file is to test the emptiness or the
missing values of a document during the registration phase
we should not allowed an empty, or a missing document value during registration
"""
from unittest import TestCase
from bmic.fixtures import dict_example
from bmic.src import dico

class TestDict(TestCase):
    """
    All of our tests to our dictionnary
    should take place here
    """
    dict = {}
    dictionnaire1= {}
    #############################################################################
    #                             Tests Fixtures                                #
    #############################################################################
    @classmethod
    def setUpClass(cls):
        TestDict.dictionnaire = {}
        TestDict.dictionnaire1 = {
        "_id": "693323272",
        "first name": "Doragorn",
        "last name": "",
        "Date of birth": "1985-07-05",
        "weight": "80",
        "height": "1.74"
    }


    #############################################################################
    #                             Our Tests                                     #
    #############################################################################

    def test_dict_emptiness(self):
        """
        Test to check if the dictionnary is empty
        """
        self.assertEqual(dico.dict_emptiness(TestDict.dictionnaire), 0)

    def test_check_missing_values(self):
        """
        The dict to pass to registration form should not contain
        empty values
        """
        self.assertEqual(dico.check_missing_value(TestDict.dictionnaire1), True)

    def test_get_empty_values(self):
        """
        For the registration we need to know what are the empty values
        so that we can alert the user to fill them
        """
        self.assertGreaterEqual(len(dico.get_empty_values(TestDict.dictionnaire1)), 1)