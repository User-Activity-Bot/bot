from os import getenv
import requests

from app.backend.routes import Routes



def user_get_or_create(chat_id : str):
    response = requests.get(Routes.user_get_or_create.format(chat_id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def create_actions(data):
    response = requests.post(url=Routes.create_actions,
                             json=data)

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}

def success_payment(payment_id : str):
    response = requests.patch(Routes.success_payment.format(payment_id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def get_action_by_user(chat_id : str):
    response = requests.get(Routes.get_action_by_user.format(chat_id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def get_daily_report(chat_id : str):
    response = requests.get(Routes.get_daily_report.format(chat_id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def action_by_id(id : str):
    response = requests.get(Routes.action_by_id.format(id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def change_alert_status(track_id : str, chat_id : str):
    response = requests.get(Routes.change_alert_status.format(track_id, chat_id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def get_usage_statistic():
    response = requests.get(Routes.usage_statistic)

    if response.status_code != 200 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}

def post_add_counter(chat_id : str, type : str, data : str):
    response = requests.post(url=Routes.add_counter,
                             json={"user_id": f"{chat_id}", 
                                   "type": f"{type}", 
                                   "data": f"{data}"
                                   })

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}

def post_add_regular(chat_id : str, interval : str):
    response = requests.post(url=Routes.add_regular,
                             json={"user_id": f"{chat_id}", 
                                   "interval": interval, 
                                   })

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}

def post_add_referral(chat_id : str, ref_id : str):
    response = requests.post(url=Routes.add_referral,
                             json={"user_id": f"{chat_id}", 
                                   "ref_id": ref_id, 
                                   })

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}

def get_referral_data(ref_id : str):
    response = requests.get(Routes.get_referral.format(ref_id))
    
    if response.status_code != 200:
        return {"status" : False}
    
    return {"status" : True, "result" : response.json()}

def post_add_referral_url(name : str):
    response = requests.post(url=Routes.add_referral_url,
                             json={"name": f"{name}", 
                                   })

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}


def get_referral_url():
    response = requests.get(url=Routes.list_referral_url)

    if response.status_code != 200 and response.status_code != 201 and response.status_code != 404:
        return {"status" : False}
    elif response.status_code == 404:
        return {"status" : False, "error" : "404"}

    return {"status" : True, "result" : response.json()}