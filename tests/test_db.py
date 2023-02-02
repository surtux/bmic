"""All the tests on Cloudant db willl take place here"""
from unittest import TestCase
from bmic.src import keys, db
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

INFO = {}
class TestDb(TestCase):
    """The test on our db will take place here"""
    @classmethod
    def setUpClass(cls):
        """Test Fixture. Will be executed before all tests"""
        #Those three lines, allowed us to connect to the cloudant endpoint
        global INFO
        auth = db.authenticate_db()
        database = db.create_db("baba", auth)
        database1 = db.create_db("bobo", auth)
        with open("./fixtures/data.json") as record:
            INFO = json.load(record) 

    def test_create_db(self):
        """
        Our first test. Should create a db and check if it has
        really been created on IBM cloud instance 
        """
        self.assertEqual(database, True)
    
    def test_delete_db(self):
        """
        Our second test. Should delete the db create from the previous
        test
        """
        self.assertEqual(db.delete_db("bobo"), True)
    def test_insert_doc(self):
        """
        We are going to test insertion into cloudant
        Basically will insert a record, and then check if the record
        is recorded
        """
        global INFO
        doc = 