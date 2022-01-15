import requests
import json


class Labirint:
    def __init__(self):
        self.base_url = "https://www.labirint.ru/"

    def get_main_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def get_book_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url +"books/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_best_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "best/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_school_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "best/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_games_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "games/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_office_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "office/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_club_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "club/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_cabinet_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "cabinet/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_putorder_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "cabinet/putorder/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_cart_page(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url + "cart/", params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_books(self, filter: str = ""):
        filter = {'filter': filter}
        res = requests.get(self.base_url, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result