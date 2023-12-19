import requests

sheety_api_link = {
    'Trilochans_Family': "https://script.google.com/macros/s/AKfycbz1559ybBDr86qSpW4mtvowVTvQMRSZ8RZeUIL0oL5D2F9HDLI6D4ZIoYoreCFZUSyj/exec",   # google sheet link :- https://docs.google.com/spreadsheets/d/12xwcs7nLX_dY_kVmP9ZgrAohL-VWlDkEHCYTjDpbNqk/edit?usp=sharing
    # 'test file': 'https://script.google.com/macros/s/AKfycbyeQBi7hlwl1jnG4P-Nc1_tJVDcKubuDhWtZ-15l2iWl9ySK3MHfcdXGKlvreaB6pra-A/exec',       # google sheet link:-  https://docs.google.com/spreadsheets/d/1808jKypQ3On8PXkEaIuE-9HOVQW6atQYVVuojk2N1Nw/edit?usp=sharing
}


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

