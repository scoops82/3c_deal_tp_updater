# You will need to run the following command before running the script for the first time:
# pip install py3cw
#
# For this script to work, the bot titles you want to update must contain 'SDCA' in the title
#
# Run using this command from within the same folder:
# python3 tp_updater.py

from py3cw.request import Py3CW

p3cw = Py3CW(
    key='',     #your 3Commas API key
    secret='',  #Your 3Commas secret key
    request_options={
        'request_timeout': 10,
        'nr_of_retries': 1,
        'retry_status_codes': [502]
    }
)

error, data = p3cw.request(
    entity='deals',
    action='',
    payload={
        "limit": 500,
        "scope": 'active',
    }
)

active_spot_deals = []

for deal in data:
    if deal["closed_at"] == None and "SDCA" in deal["bot_name"]:
        active_spot_deals.append(deal)
        
for deal in active_spot_deals:
    if deal["completed_safety_orders_count"] == 3 and deal["take_profit"] != 1.00:
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal["id"]),
            payload={
                "deal_id": deal["id"],
                "take_profit": 1.00,
            }     
        )
        print(str(deal["id"]) + " " + deal["pair"] + " updated TP to 1%")
    elif deal["completed_safety_orders_count"] == 4 and deal["take_profit"] != 2.00:
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal["id"]),
            payload={
                "deal_id": deal["id"],
                "take_profit": 2.00,
            }     
        )
        print(str(deal["id"]) + " " + deal["pair"] + " updated TP to 2%")
    elif deal["completed_safety_orders_count"] == 5 and deal["take_profit"] != 3.00:
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal["id"]),
            payload={
                "deal_id": deal["id"],
                "take_profit": 3.00,
            }     
        )
        print(str(deal["id"]) + " " + deal["pair"] + " updated TP to 3%")
    elif deal["completed_safety_orders_count"] == 6 and deal["take_profit"] != 4.00:
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal["id"]),
            payload={
                "deal_id": deal["id"],
                "take_profit": 4.00,
            }     
        )
        print(str(deal["id"]) + " " + deal["pair"] + " updated TP to 4%")
    elif deal["completed_safety_orders_count"] == 7 and deal["take_profit"] != 5.00:
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal["id"]),
            payload={
                "deal_id": deal["id"],
                "take_profit": 5.00,
            }     
        )
        print(str(deal["id"]) + " " + deal["pair"] + " updated TP to 5%")
    elif deal["completed_safety_orders_count"] == 8 and deal["take_profit"] != 6.00:
        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal["id"]),
            payload={
                "deal_id": deal["id"],
                "take_profit": 6.00,
            }     
        )
        print(str(deal["id"]) + " " + deal["pair"] + " updated TP to 6%")
    else:
        print(str(deal["id"]) + " " + deal["pair"] + " TP up to date!")

