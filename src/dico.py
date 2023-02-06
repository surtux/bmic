"""
This module is use to test is the document is empty
we should not register an empty document or a document
with a missing key
"""

def dict_emptiness(dictionnaire):
    """
    We are
    """
    return len(dictionnaire)

def check_missing_value(dictionnaire):
    """
    We are testing for the pupose of registration form
    to see if the doc contain missing value(s).
    We shouldn't allow this previous scenario
    """
    answer = False
    for value in dictionnaire.values():
        if value == "":
            answer = True
            break
    return answer
