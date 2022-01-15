import requests
import json
from API_labirint import Labirint

labirint = Labirint()

#1 Тест API главной страницы
def test_get_main_page():
    status = labirint.get_main_page()
    assert status == 200


#2 Test API of the "books" page
def test_get_books_page():
    status = labirint.get_book_page()
    assert status == 200

#3 Test API of the "best" page
def test_get_best_page():
    status = labirint.get_best_page()
    assert status == 200

#4 Test API of the "school" page
def test_get_school_page():
    status = labirint.get_school_page()
    assert status == 200

#5 Test API of the "games" page
def test_get_games_page():
    status = labirint.get_games_page()
    assert status == 200

#6 Test API of the "office" page
def test_get_office_page():
    status = labirint.get_office_page()
    assert status == 200

#7 Test API of the "club" page
def test_get_club_page():
    status = labirint.get_club_page()
    assert status == 200

#8 Test API of the "cabinet" page
def test_get_cabinet_page():
    status = labirint.get_cabinet_page()
    assert status == 200

#9 Test API of the "putorder" page
def test_get_putorder_page():
    status = labirint.get_putorder_page()
    assert status == 200

#10 Test API of the "cart" page
def test_get_cart_page():
    status = labirint.get_cart_page()
    assert status == 200

#11
def test_get_all_books_with_empty_filter(filter=''):
    status = labirint.get_list_of_books( filter)
    assert status == 200

#12
def test_get_all_books_with_uncorrect_filter(filter='мороз'):
    status = labirint.get_list_of_books( filter)
    assert status != 200

#13
def test_get_all_books_with_too_long_filter(filter='мороз' * 1000):
    status = labirint.get_list_of_books(filter)
    assert status != 200

#14
def test_get_all_books_with_255letter_filter(filter='мороз' * 51):
    status = labirint.get_list_of_books( filter)
    assert status != 200

#15
def test_get_all_books_with_symbol_filter(filter='@#$%$$#'):
    status = labirint.get_list_of_books( filter)
    assert status != 200

#16
def test_get_labirunt_appstore():
    status = labirint.get_labirint_appstore()
    assert status == 200

#17
def test_get_labirint_vkontakte():
    status = labirint.get_labirint_vkontakte()
    assert status == 200

#18
def test_get_labirint_google_play():
    status = labirint.get_labirint_google_play()
    assert status == 200

#19
def test_get_labirint_app_gallery():
    status = labirint.get_labirint_app_gallery()
    assert status == 200

#20
def test_get_labirint_vkontakte_deti():
    status = labirint.get_labirint_vkontakte_dety()
    assert status == 200

#21
def test_get_labirint_youtube():
    status = labirint.get_labirint_youtube()
    assert status == 200

#22
def test_get_labirint_instagram():
    status = labirint.get_labirint_instagram()
    assert status == 200

#23
def test_get_labirint_instagram_deti():
    status = labirint.get_labirint_instagram_deti()
    assert status == 200

#24
def test_get_labirint_facebook():
    status = labirint.get_labirint_fasebook()
    assert status == 200

#25
def test_get_labirint_odnoklassniki():
    status = labirint.get_labirint_odnoklasniki()
    assert status

#26
def test_get_labirint_twitter():
    status = labirint.get_labirint_twitter()
    assert status

#27
def test_get_labirint_zen():
    status = labirint.get_labirint_zen()
    assert status

#28
def test_get_labirint_telegram():
    status = labirint.get_labirint_telegram()
    assert status

#29
def test_get_labirint_tiktok():
    status = labirint.get_labirint_tiktok()
    assert status

#30
def test_get_labirint_partners():
    status = labirint.get_labirint_partners()
    assert status

#31
def test_get_labirint_vakansii():
    status = labirint.get_labirint_vakansii()
    assert status



