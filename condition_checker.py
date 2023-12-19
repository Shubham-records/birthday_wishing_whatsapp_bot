from datetime import datetime
from google_sheet_api import SheetApi
from random import choice

data = SheetApi()

with open('anniversary_quotes.txt') as r:
    anniversary_quotes = r.readlines()
with open('birthday_quotes.txt') as r:
    birthday_quotes = r.readlines()


class Condition:
    def __init__(self):
        self.month = datetime.now().strftime("%B")
        self.day = datetime.now().day+1
        self.today_wishing_messages = []

    def birthday_check(self):
        for i in data.all_data:

            if i['birthMonth'].lower() == self.month.lower() and i['birthDay'] == self.day:
                gf = {'phoneNo': i['phoneNo'],
                      'message': f"Happy Birthday {i['familyZone'].split(' ')[0]} \n{choice(birthday_quotes).strip()}",
                      'name': i['familyZone'].split(' ')[0]}
                self.today_wishing_messages.append(gf)

    def anniversary_check(self):
        for i in data.all_data:

            if i['anniversaryMonth'].lower() == self.month.lower() and i['anniversaryDate'] == self.day:
                gf = {'phoneNo': i['phoneNo'],
                      "message": f"Happy Anniversary {i['familyZone'].split(' ')[0]} \n{choice(anniversary_quotes).strip()}",
                      'name': i['familyZone'].split(' ')[0]}
                self.today_wishing_messages.append(gf)

    def check(self):
        data.data_collector()
        self.birthday_check()
        self.anniversary_check()



