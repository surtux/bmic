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

def create_db(dbname, service):
    """
    We should first connect to the db, then
    insert the users and the informations
    """
    response = service.put_database(db=dbname, partitioned=True).get_result()
    return response['ok']

def delete_db(dbname, service):
    """
    This function is here to teardown connection to db
    """
    response = service.delete_database(db=dbname).get_result()
    return response['ok']

def insert_doc(dbname, information, service):
    """Code to insert a document in cloudant"""
    event_doc = information
    result = service.post_document(db=dbname, doc_id=id, document=event_doc).get_result()
    return result