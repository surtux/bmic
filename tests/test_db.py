"""All the tests on Cloudant db willl take place here"""
from unittest import TestCase
from bmic.src import keys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
class TestDb(TestCase):
    """The test on our db will take place here"""
    @classmethod
    def setUpClass(cls):
        AUTHENTICATOR = IAMAuthenticator(keys.APIKey)
        SERVICE = CloudantV1(authenticator=AUTHENTICATOR)
        SERVICE.set_service_url('{url}')