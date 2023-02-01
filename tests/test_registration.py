"""
The purpose of this file is to test the registration of
our app
"""
from unittest import TestCase
from bmic.src import registration_ui, keys, db
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TestRegistration(TestCase):
    """The test on our db will take place here"""
    @classmethod
    def setUpClass(cls):
        """Test Fixture. Will be executed before all tests"""
        

    """This class containt the test for registration"""
    def test_registration(self):
        """
        We should connect to cloudant, create a db query the empty
        db. The result should be empty for the test to pass. Then
        we will insert a record in this db, then query the db. The
        result should be the same as the record we previously enter
        """
        self.assertEqual(db.create_db("baba"), True)
        name = db.insert_doc(name, information)
        #This line should compare the result of the insertion query with ok
        self.assertEqual(name['ok'], True)
        
        