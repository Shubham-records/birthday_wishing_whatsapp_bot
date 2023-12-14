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
        self.day = datetime.now().day
        self.today_wishing_messages = []

    def birthday_check(self):
        for i in data.all_data:
            try:
                print(i['familyZone'] + " birthday_check")
                if i['birthMonth'].lower() == self.month.lower() and i['birthDay'] == self.day:
                    gf = {'phoneNo': i['phoneNo'],
                          'message': f"Happy Birthday {i['familyZone'].split(' ')[0]} \n{choice(birthday_quotes).strip()}"}
                    self.today_wishing_messages.append(gf)

                print("success\n")

            except KeyError:
                print("got an error\nits okay\n")
                pass

    def anniversary_check(self):
        for i in data.all_data:
            try:
                print(i['familyZone'] + ' anniversary_check')
                if i['anniversaryMonth'].lower() == self.month.lower() and i['anniversaryDate'] == self.day:
                    gf = {'phoneNo': i['phoneNo'],
                          "message": f"Happy Anniversary {i['familyZone'].split(' ')[0]} \n{choice(anniversary_quotes).strip()}"}
                    self.today_wishing_messages.append(gf)
                print("success\n")

            except KeyError:
                print("got an error\nits okay\n")
                pass

    def check(self):
        data.data_collector()
        self.birthday_check()
        self.anniversary_check()





# test subjects json

# [{7008976481: 'Happy Birthday Debabrata\nI hope all your birthday wishes and dreams come true.'},
# {7008976481: 'Happy Birthday Supriya\nBe happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!'},
#  {
#      7008976481: 'Happy Birthday Aayush\nCheers to another year! Hope your day is filled with love (and lots of birthday cake).'},
#  {
#      7008976481: 'Happy Birthday Susanta\nCheers to another year! Hope your day is filled with love (and lots of birthday cake).'},
#  {
#      7008976481: 'Happy Birthday Latika\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Jibesh\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {7008976481: 'Happy Birthday Monika\nI hope all your birthday wishes and dreams come true.'}, {
#      7008976481: 'Happy Birthday Subham\nCheers to another year! Hope your day is filled with love (and lots of birthday cake).'},
#  {
#      7008976481: 'Happy Birthday Sutapa\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {7008976481: 'Happy Birthday Shaswat\nI hope all your birthday wishes and dreams come true.'}, {
#      7008976481: 'Happy Birthday Subash\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Rajashree\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Soham\nBe happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!'},
#  {
#      7008976481: 'Happy Birthday Sukumar\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Karishma\nBe happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!'},
#  {
#      7008976481: 'Happy Birthday Madhusmita-Sneha\nBe happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!'},
#  {7008976481: 'Happy Birthday Samarth\nI hope all your birthday wishes and dreams come true.'}, {
#      7008976481: 'Happy Birthday Debashis\nMay your birthday balloons be as big as your dreams, and may they both soar to brand-new heights.'},
#  {
#      7008976481: 'Happy Birthday Santanu\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Nitu\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Sriyan\nMay your birthday be the start of a year filled with good luck, good health, and much happiness.'},
#  {
#      7008976481: 'Happy Birthday Ujjal\nBe happy! Today is the day you were brought into this world to be a blessing and inspiration to the people around you! You are a wonderful person! May you be given more birthdays to fulfill all of your dreams!'},
#  {7008976481: "Happy Anniversary Debabrata\nHere's to many more years of happiness and adventures together."},
#  {7008976481: 'Happy Anniversary Supriya\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Aayush\nMay your love story continue to inspire others.'},
#  {7008976481: 'Happy Anniversary Susanta\nWishing you a lifetime of love and happiness together.'},
#  {7008976481: 'Happy Anniversary Latika\nWishing you a lifetime of love and happiness together.'},
#  {7008976481: 'Happy Anniversary Jibesh\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Monika\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Subham\nWishing you a lifetime of love and happiness together.'},
#  {7008976481: 'Happy Anniversary Sutapa\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Shaswat\nWishing you a lifetime of love and happiness together.'},
#  {7008976481: 'Happy Anniversary Subash\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Rajashree\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Soham\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Sukumar\nWishing you a lifetime of love and happiness together.'},
#  {7008976481: "Happy Anniversary Karishma\nHere's to many more years of happiness and adventures together."},
#  {7008976481: 'Happy Anniversary Madhusmita-Sneha\nWishing you a lifetime of love and happiness together.'},
#  {7008976481: 'Happy Anniversary Samarth\nMay your love story continue to inspire others.'},
#  {7008976481: 'Happy Anniversary Debashis\nMay your love continue to grow stronger with each passing year.'},
#  {7008976481: 'Happy Anniversary Santanu\nCheers to another year of love, laughter, and joy!'},
#  {7008976481: 'Happy Anniversary Nitu\nCheers to another year of love, laughter, and joy!'},
#  {7008976481: 'Happy Anniversary Sriyan\nMay your love story continue to inspire others.'},
#  {7008976481: 'Happy Anniversary Ujjal\nCheers to another year of love, laughter, and joy!'}]
