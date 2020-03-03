import twilio
import pickle
from datetime import date
import os
import json
def setup():
    "sets up twilio, must be done before running any twilio function"
    from twilio.rest import Client
    twi = readfromfile("twilioinfo.json")
    """twilioinfo.json should look like this:
    [
    "account_sidgoes here",
    "auth_token goes here"
    ]
    
    """

    account_sid = twi[0]
    auth_token = twi[1]
    client = Client(account_sid, auth_token)
    return client

def send_message(bod,num,client):
    """sends a string to phone number
    bod is string message
    num is the string phonenumber in the form '+##########' with areas code included
    setup must be run before this function"""

    message = client.messages \
        .create(
        body=bod,
        from_='+14436711087',
        to=num
    )

def writeArraytofile(a,pat):
    with open(pat,"w") as txt:
        json.dump(a,txt,ensure_ascii=False, indent=4)

def readfromfile(pat):
    with open(pat,"rb") as txt:
        b = json.load(txt)
    return b

def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]


def rearrange_data(pat):
    """ takes an array with last weeks information and adjusts it to the present
    info type: array"""
    if os.path.exists(pat):
        a = readfromfile(pat)
        b = shift(a)
        writeArraytofile(b)
    else:
        print("File not found, creating file...")
        writeArraytofile(["Kitchen","First floor Bathroom","2nd Floor Bathroom","Garbage 1","Garbage 2"],pat)
        #when we have 6 roommates the roles need to change here and a "free" role needs to be added
def mainthing():
    client = setup()
    users = readfromfile("users.json")

    if date.today().isoweekday() == 5: # day is firday
        rearrange_data("schedule.txt")# file needs to be changed for server, maybe
        a = readfromfile("schedule.txt")
        for num in range(len(a)):
            if a[num] != "Garbage 1" or "Garbage 2" or "Free":
                msg = "Hi "+users[num]["Name"] +"This week you are cleaning the "+a[num]
                send_message(msg,users[num]["Number"],client)

    elif date.today().isoweekday() == 1: # day is monday
        a = readfromfile("schedule.txt")

        for num in range(len(a)):
            if a[num] == "Garbage 1":
                Gp1 = num
            elif a[num] == "Garbage 2":
                Gp2 = num
        msg1 = "Hi "+users[Gp1]["Name"] +"This week you are cleaning the Garbage with "+users[Gp2]["Name"]
        msg2 = "Hi "+users[Gp2]["Name"] +"This week you are cleaning the Garbage with "+users[Gp1]["Name"]
        send_message(msg1,users[Gp1]["Number"],client)
        send_message(msg2,users[Gp2]["Number"],client)





"""Legend
0 - Jack
1 - Skyla
2 - Sarah
3 - Chris
4 - Natasha
Chores
0 - Kitchen
1 - First floor bathroom
3 - 2nd floor bathroom
3 - Garbage 1
4 - Garbage 2

a = ["Kitchen","First floor Bathroom","2nd Floor Bathroom","Garbage 1","Garbage 2"]
"""











#client = setup()
#send_message(input("Please type message: "),'+***REMOVED***')
