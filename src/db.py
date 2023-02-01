"""
This python file will be use to manipulate ou remote IBM db
so that we can store all the relate bmi information of users
"""
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import keys


def authenticate_db():
    """You should first authenticate"""
    authenticator = IAMAuthenticator(keys.APIKEY)
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url(keys.URL)
    return service

def create_db(name):
    """
    We should first connect to the db, then then
    insert the users and the informations
    """
    auth = authenticate_db()
    response = auth.put_database(db=name, partitioned=True).get_result()
    return response['ok']

def delete_db(name):
    """
    This function is here to teardown connection to db
    """
    auth = authenticate_db()
    response = auth.delete_database(db=name).get_result()
    return response['ok']
