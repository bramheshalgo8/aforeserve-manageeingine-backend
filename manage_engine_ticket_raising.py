import json
import requests
import config
import configparser
config = configparser.ConfigParser()
config.read('config_test.ini')
def ticket_raising(subject, description, requester_name, requester_id):
    print("hello")
    URL = config["DEFAULT"]["api link"]
    header = {"Authtoken": config["DEFAULT"]["token"]}

    data = {"input_data": json.dumps({
        "request": {
            "subject": subject,
            "description": description,
             "requester": {
                "id": requester_id,
                "name": requester_name
            }
        }
    })}
    # config.logger.info('Requesting to add new request')
    r = requests.post(url = URL, headers=header, data = data, verify=False)
    print(r.json)
    # config.logger.info('Request added')
    return  r.json()

# s = ticket_raising("Password reset","My password needs to be reset","Sunny Singh","301")