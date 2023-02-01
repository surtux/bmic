"""
The code contain in this file will be use to write content in cloudant
"""
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from db import create_db

DATABASE = create_db("toto")
#The code below will insert data in the database create above
