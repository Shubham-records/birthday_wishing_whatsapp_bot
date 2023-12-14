import requests

sheety_api_link = {
    'Trilochans_Family': "https://script.google.com/macros/s/AKfycbz1559ybBDr86qSpW4mtvowVTvQMRSZ8RZeUIL0oL5D2F9HDLI6D4ZIoYoreCFZUSyj/exec",   # google sheet link :- https://docs.google.com/spreadsheets/d/12xwcs7nLX_dY_kVmP9ZgrAohL-VWlDkEHCYTjDpbNqk/edit?usp=sharing
    # 'test file': 'https://script.google.com/macros/s/AKfycbyeQBi7hlwl1jnG4P-Nc1_tJVDcKubuDhWtZ-15l2iWl9ySK3MHfcdXGKlvreaB6pra-A/exec',       # google sheet link:-  https://docs.google.com/spreadsheets/d/1808jKypQ3On8PXkEaIuE-9HOVQW6atQYVVuojk2N1Nw/edit?usp=sharing
}
# here i use google app script api to get data from sheets
# if i explian to you about app script
# like mmm, if you have webapp, you code the interfarace from tkinter, database = google sheet or drive or whatever google workshop have,
# and app script is making an api, or bridge between them, we can request upto 250/day
# its better from google console, because first $300 free trail than paid
# and its better than sheety api, because 200 requests per month.


# i like to run the link of the app script in your webbrowser first, because its require authentication first.

class SheetApi:
    def __init__(self):
        self.all_data = []

    def data_collector(self):
        for i in sheety_api_link:
            output = requests.get(sheety_api_link[i])
            output = output.json()

            for no_of_sheets in output:

                for sheet_data in output[no_of_sheets][1:]:
                    self.all_data.append(sheet_data)


sheet = SheetApi()
sheet.data_collector()
print(sheet.all_data)

# [{'familyZone': 'Debabrata Patra', 'birthMonth': 'July', 'birthDay': 16, 'anniversaryMonth': 'May', 'anniversaryDate': 9, 'phoneNo': 6370688349},
#  {'familyZone': 'Supriya Ghosh', 'birthMonth': '', 'birthDay': '', 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': ''},
#  {'familyZone': 'Aayush Patra', 'birthMonth': 'March', 'birthDay': 27, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': ''},
#  {'familyZone': 'Susanta Ghosh', 'birthMonth': 'August', 'birthDay': 18, 'anniversaryMonth': 'October', 'anniversaryDate': 22, 'phoneNo': 9693344132},
#  {'familyZone': 'Latika Patra', 'birthMonth': 'March', 'birthDay': 10, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 6201237538},
#  {'familyZone': 'Jibesh Ghosh', 'birthMonth': 'August', 'birthDay': 10, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8986602728},
#  {'familyZone': 'Monika Patra', 'birthMonth': 'December', 'birthDay': 19, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 7008976481},
#  {'familyZone': 'Subham Pal', 'birthMonth': 'March', 'birthDay': 31, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8249660983},
#  {'familyZone': 'Sutapa Patra', 'birthMonth': 'July', 'birthDay': 14, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8144971439},
#  {'familyZone': 'Shaswat Mondal', 'birthMonth': 'April', 'birthDay': 6, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8144971439},
#  {'familyZone': 'Subash Patra', 'birthMonth': 'January', 'birthDay': 23, 'anniversaryMonth': 'May', 'anniversaryDate': 6, 'phoneNo': 9539111662},
#  {'familyZone': 'Rajashree Kalia', 'birthMonth': 'May', 'birthDay': 30, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 9778744893},
#  {'familyZone': 'Soham Patra', 'birthMonth': 'December', 'birthDay': 3, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 9778744893},
#  {'familyZone': 'Sukumar Palei', 'birthMonth': 'December', 'birthDay': 6, 'anniversaryMonth': 'February', 'anniversaryDate': 24, 'phoneNo': ''},
#  {'familyZone': 'Karishma Patra', 'birthMonth': 'May', 'birthDay': 7, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8260032248},
#  {'familyZone': 'Madhusmita-Sneha', 'birthMonth': 'January', 'birthDay': 23, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8260032248},
#  {'familyZone': 'Samarth Palei', 'birthMonth': 'November', 'birthDay': 16, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8260032248},
#  {'familyZone': 'Debashis Patra', 'birthMonth': 'November', 'birthDay': 8, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 8984150119},
#  {'familyZone': 'Santanu Pal', 'birthMonth': 'July', 'birthDay': 26, 'anniversaryMonth': 'October', 'anniversaryDate': 30, 'phoneNo': ''},
#  {'familyZone': 'Nitu Patra', 'birthMonth': 'February', 'birthDay': 18, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': 7328860663},
#  {'familyZone': 'Sriyan Pal', 'birthMonth': 'October', 'birthDay': 26, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': ''},
#  {'familyZone': 'Ujjal Patra', 'birthMonth': 'November', 'birthDay': 21, 'anniversaryMonth': '', 'anniversaryDate': '', 'phoneNo': ''}]
