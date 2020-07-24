import requests
import json
import config
import pandas as pd
import create_db
def ticket_updation(df):
    for i in range(len(df)):
        config.logger.info('Fetching ticket')
        inc_id = df.iloc[i]['Incident ID']
        data = {"input_data":json.dumps({
            "request": {
               "status": {
                    "name": "Resolved"
                },
                'status_change_comments': "Issue has been successfully resolved"
            }}) }
        URL= "https://182.75.252.43:8080/api/v3/requests/" + str(inc_id)
        header = {"Authtoken": "A8827317-282E-4BAF-B788-C6E830B2F934"}
        r1 = requests.put(url = URL, verify= False, headers=header, data = data)
        config.logger.info('Ticket status changed')
    return r1.json()

def updatetickets(ticket_id,status,solution):
    config.logger.exception("In update ticket part")
    query = "select * from tickets where `Incident ID` = '"+ticket_id+"';"
    df=create_db.fetchquery(query)
    df.loc[df["Incident ID"]==ticket_id , 'Status'] = status
    df.loc[df["Incident ID"]==ticket_id , 'Solution'] = solution
    print(df)
    ret = create_db.update(df)
    config.logger.exception('data updated in db')

    ticket_updation(df.loc[df.Status =="Resolved"]) 
    config.logger.exception('ticket updated in itsm')


# s = ticket_updation(df)