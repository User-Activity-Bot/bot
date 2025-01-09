from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Routes:
    BACK_URL = getenv("BACK_URL")
    
    user_get_or_create = f"{BACK_URL}users/?user_id={{}}"
    
    create_actions = f"{BACK_URL}actions/create/"
    
    success_payment = f"{BACK_URL}payments/{{}}/success/"
    
    get_action_by_user = f"{BACK_URL}actions/users/{{}}/"
    
    get_daily_report = f"{BACK_URL}actions/daily/?username={{}}"
    
    usage_statistic = f"{BACK_URL}counter/count/"
    
    add_counter = f"{BACK_URL}counter/"
    
    add_regular = f"{BACK_URL}regular/horoscope/"
    
    add_referral = f"{BACK_URL}referral/create/"
    get_referral = f"{BACK_URL}referral/data?ref_id={{}}"
    
    add_referral_url = f"{BACK_URL}referral/urls/create/"
    list_referral_url = f"{BACK_URL}referral/urls/list/"