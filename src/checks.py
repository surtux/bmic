"""
This module will contain all the check on ui component of
the main application and also other checks
"""

bad_password_list = ['pistache','macabo','patate','chevre','1234','tomate','janvier']

def check_password(password):
    rep_list = []
    if type(password) is list:
        for element in password:
            rep = element in bad_password_list
            rep_list.append(rep)
    if type(password) is str:
        return password in bad_password_list
    return rep_list