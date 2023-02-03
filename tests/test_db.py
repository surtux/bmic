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
        "password": "jujube"
    }
class TestDb(TestCase):
    """The test on our db will take place here"""
    database1 = False
    database2 = False
    auth = db.authenticate_db()
    @classmethod
    def setUpClass(cls):
        """Test Fixture. Will be executed before all tests"""
        #Those three lines, allowed us to connect to the cloudant endpoint
        global INFO
        TestDb.database1 = db.create_db("baba", TestDb.auth)
        TestDb.database2 = db.create_db("bobo", TestDb.auth)
        #with open("./fixtures/data.json") as record:
        #    INFO = json.load(record)
    @classmethod
    def tearDown(cls):
        """Method to clean everything after all the test passes"""
        toto = db.delete_db("baba", TestDb.auth)

    def tearDown(self):
        """I try to close a db after all the tests cases passed"""
        
    
    ###########################################################################
    #                          TESTS CASES                                    #
    ###########################################################################            


    def test_create_db(self):
        """
        Our first test. Should create a db and check if it has
        really been created on IBM cloud instance 
        """
        self.assertEqual(TestDb.database1, True)
    
    def test_delete_db(self):
        """
        Our second test. Should delete the db create from the previous
        test
        """
        self.assertEqual(db.delete_db("bobo", TestDb.auth), True)
    def test_insert_doc(self):
        """
        We are going to test insertion into cloudant
        Basically will insert a record, and then check if the record
        is recorded
        """
        global INFO
        self.assertEqual(db.insert_doc("baba", INFO, TestDb.auth), True)
    def test_get_record(self):
        """
        We are going to retrieve document from cloudant db 
        """
        self.assertEqual(db.get_record(identity, password, TestDb.auth), True)