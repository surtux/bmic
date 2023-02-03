"""
This python file will be use to manipulate ou remote IBM db
so that we can store all the relate bmi information of users
"""
from ibmcloudant.cloudant_v1 import CloudantV1, Document
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
    """
    Code to insert a document in cloudant. This method should be
    called in conjunction with registration windows only
    """
    #Warning! The parameter of Document Method is not a Dictionnary
    #This condition is used to check if it is a registered user. If the case, just update his bmi
    if bool(get_record(information["_id"], dbname, service)):
        event_doc = Document(
            id=information["_id"],
            weight=information["weight"],
            height=information["height"],
            bmi=information["bmi"]
        )
    else:
        #The user is not registered, so he should do it first
        event_doc = Document(
            id=information["_id"],
            first_name=information["first name"],
            last_name=information["last name"],
            Date_of_birth=information["Date of birth"],
            weight=information["weight"],
            height=information["height"],
            password=information["password"]
        )
    result = service.post_document(dbname, event_doc).get_result()
    return result["ok"]

def get_record(identity, name, service):
    """
    This function query the db for a specific record
    """
    result = service.post_all_docs(
        db=name,
        include_docs=True,
        start_key=identity,
        limit=1
    )
    return bool(result)
