import requests
import json

base_url = "https://www.labirint.ru/"
class Labirint:
    def __init__(self):
        self.base_url = "https://www.labirint.ru/"

    def get_main_page(self):
        res = requests.get(self.base_url)
        status = res.status_code
        return status

    def get_book_page(self):
        res = requests.get(self.base_url +"books/")
        status = res.status_code
        return status

    def get_best_page(self):
        res = requests.get(self.base_url +"best/")
        status = res.status_code
        return status

    def get_school_page(self):
        res = requests.get(self.base_url + "best/")
        status = res.status_code
        return status

    def get_games_page(self):
        res = requests.get(self.base_url + "games/")
        status = res.status_code
        return status

    def get_office_page(self):
        res = requests.get(self.base_url + "office/")
        status = res.status_code
        return status

    def get_club_page(self):
        res = requests.get(self.base_url + "club/")
        status = res.status_code
        return status

    def get_cabinet_page(self):
        res = requests.get(self.base_url + "cabinet/")
        status = res.status_code
        return status

    def get_putorder_page(self):
        res = requests.get(self.base_url + "cabinet/putorder/")
        status = res.status_code
        return status

    def get_cart_page(self):
        res = requests.get(self.base_url + "cart/")
        status = res.status_code
        return status

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

    def get_labirint_appstore(self):
        res = requests.get("https://apps.apple.com/ru/app/%D0%BB%D0%B0%D0%B1%D0%B8%D1%80%D0%B8%D0%BD%D1%82-%D1%80%D1%83-%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9-%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD/id1008650482")
        status = res.status_code
        return status

    def get_labirint_vkontakte(self):
        res = requests.get("https://vk.com/labirint_ru")
        status = res.status_code
        return status

    def get_labirint_google_play(self):
        res = requests.get("https://play.google.com/store/apps/details?id=ru.labirint.android")
        status = res.status_code
        return status

    def get_labirint_app_gallery(self):
        res = requests.get("https://appgallery.huawei.com/app/C101184737?appId=C101184737&source=appshare&subsource=C101184737")
        status = res.status_code
        return status

    def get_labirint_vkontakte_dety(selfs):
        res = requests.get("https://vk.com/labirintdeti")
        status = res.status_code
        return status

    def get_labirint_youtube(self):
        res = requests.get("https://www.youtube.com/user/labirintruTV")
        status = res.status_code
        return status

    def get_labirint_instagram(self):
        res = requests.get("https://www.instagram.com/labirintru/")
        status = res.status_code
        return status

    def get_labirint_instagram_deti(self):
        res = requests.get("https://www.instagram.com/labirintdeti/")
        status = res.status_code
        return status
    def get_labirint_fasebook(self):
        res = requests.get("https://www.facebook.com/labirintru")
        status = res.status_code
        return status

    def get_labirint_odnoklasniki(self):
        res = requests.get("https://ok.ru/labirintru")
        status = res.status_code
        return status

    def get_labirint_twitter(self):
        res = requests.get("https://twitter.com/labirint_ru")
        status = res.status_code
        return status

    def get_labirint_zen(self):
        res = requests.get("https://zen.yandex.ru/labirintru")
        status = res.status_code
        return status

    def get_labirint_telegram(self):
        res = requests.get("https://t.me/labirintru")
        status = res.status_code
        return status

    def get_labirint_tiktok(self):
        res = requests.get("https://www.tiktok.com/@labirintru")
        status = res.status_code
        return status

    def get_labirint_partners(self):
        res = requests.get("https://partner.labirint.ru/login")
        status = res.status_code
        return status

    def get_labirint_vakansii(self):
        res = requests.get("https://www.labirint.org/vakansii?tab=5")
        status = res.status_code
        return status





