from os import getenv

def is_admin(chat_id):
    admins_ids = getenv("ADMINS").split(",")
    
    return str(chat_id) in admins_ids 