import twilio
import pickle
from datetime import date
import os
def setup():
    "sets up twilio, must be done before running any twilio function"
    from twilio.rest import Client

    account_sid = "ACa971456efc536e1f853090003309c916"
    auth_token = "ba7834b48e0835fb81a4f74d56bd1340"
    client = Client(account_sid, auth_token)
    return client

def send_message(bod,num):
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
def determineday():
    """ check if date is friday or monday, return 1 if friday and 2 if monday, else returns 0"""
    day = date.today()


    rvalue = 0
    if day.isoweekday() == 1:
        rvalue = 2
    elif day.isoweekday() == 5:
        rvalue = 1
    else:
        rvalue = 0

    return rvalue

def writeArraytofile(a,pat):
    with open(pat,"wb") as txt:
        pickle.dump(a,txt)

def readfromfile(pat):
    with open(pat,"rb") as txt:
        b = pickle.load(txt)
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
        print("INVALID FILE")
def mainthing():


# a should be similar to {"Jack":"Kitchen","Skyla":"1st floor bathroom","Sarah":"2nd Floor Bathroom","Chris":"Garbage 1","natasha":"Garbage 2"}
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

a = [0,1,2,3,4]
"""











#client = setup()
#send_message(input("Please type message: "),'+***REMOVED***')
