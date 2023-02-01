"""All the tests on Cloudant db willl take place here"""
from unittest import TestCase
from bmic.src import keys, db
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
class TestDb(TestCase):
    """The test on our db will take place here"""
    @classmethod
    def setUpClass(cls):
        """Test Fixture. Will be executed before all tests"""
        #Those three lines, allowed us to connect to the cloudant endpoint
        AUTHENTICATOR = IAMAuthenticator(keys.APIKEY)
        SERVICE = CloudantV1(authenticator=AUTHENTICATOR)
        SERVICE.set_service_url(keys.URL)
    
    @classmethod
    def tearDownClass():
        """
        Will be executed after all tests have been run
        """

    def test_create_db(self):
        """
        Our first test. Should create a db and check if it has
        really been created on IBM cloud instance 
        """
        self.assertEqual(db.create_db("goofy"), True)