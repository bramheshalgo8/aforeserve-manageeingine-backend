import json
import requests
import config

def ticket_raising(subject, description, requester_name, requester_id):
    URL = "https://182.75.252.43:8080/api/v3/requests"
    header = {"Authtoken": "A8827317-282E-4BAF-B788-C6E830B2F934"}

    data = {"input_data": json.dumps({
        "request": {
            "subject": subject,
            "description": description,
             "requester": {
                "id": requester_id,
                "name": requester_name
            },
            "status": {
                "name": "New"
            }
        }
    })}
    config.logger.info('Requesting to add new request')
    r = requests.post(url = URL, headers=header, data = data, verify=False)
    config.logger.info('Request added')
    return  r.json()

# s = ticket_raising("Password reset","My password needs to be reset","Sunny Singh","301")