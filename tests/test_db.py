"""All the tests on Cloudant db willl take place here"""
from unittest import TestCase
from bmic.src import keys, db
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

INFO = {
        "_id": "doudou:693323272",
        "first name": "Doragorn",
        "last name": "Coucout",
        "Date of birth": "1985-07-05",
        "weight": "80",
        "height": "1.74",
        "password": "jujube",
        "bmi": "25.75"
    }
class TestDb(TestCase):
    ##########################################################################
    #                          TESTS FIXTURES                                #
    ##########################################################################
    
    """The test on our db will take place here"""
    database1 = False
    auth = db.authenticate_db()
    @classmethod
    def setUpClass(cls):
        """Test Fixture. Will be executed before all tests"""
        #Those three lines, allowed us to connect to the cloudant endpoint
        global INFO
        TestDb.database1 = db.create_db("baba", TestDb.auth)

    ###########################################################################
    #                          TESTS CASES                                    #
    ###########################################################################            


    def test_create_db(self):
        """
        Our first test. Should create a db and check if it has
        really been created on IBM cloud instance 
        """
        self.assertEqual(TestDb.database1, True)
    
    def test_get_record(self):
        """
        We are going to retrieve document from cloudant db 
        """
        global INFO
        db.insert_doc("baba", INFO, TestDb.auth)
        self.assertEqual(db.get_record(INFO["_id"], "baba", TestDb.auth), True)
        db.delete_db("baba", TestDb.auth)