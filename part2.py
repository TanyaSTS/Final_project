import requests
import json
from API_labirint import Labirint

labirint = Labirint()

#1 Тест API главной страницы
def test_get_main_page(filter=''):
    status = labirint.get_main_page( filter)
    assert status == 200


#2 Test API of the "books" page
def test_get_books_page(filter=''):
    status = labirint.get_book_page( filter)
    assert status == 200

#3 Test API of the "best" page
def test_get_best_page(filter=''):
    status = labirint.get_best_page( filter)
    assert status == 200

#4 Test API of the "school" page
def test_get_school_page(filter=''):
    status = labirint.get_school_page( filter)
    assert status == 200

#5 Test API of the "games" page
def test_get_games_page(filter=''):
    status = labirint.get_games_page( filter)
    assert status == 200

#6 Test API of the "office" page
def test_get_office_page(filter=''):
    status = labirint.get_office_page( filter)
    assert status == 200

#7 Test API of the "club" page
def test_get_club_page(filter=''):
    status = labirint.get_club_page( filter)
    assert status == 200

#8 Test API of the "cabinet" page
def test_get_cabinet_page():
    status = labirint.get_cabinet_page( filter)
    assert status == 200

#9 Test API of the "putorder" page
def test_get_putorder_page(filter=''):
    status = labirint.get_putorder_page( filter)
    assert status == 200

#10 Test API of the "cart" page
def test_get_cart_page(filter=''):
    status = labirint.get_cart_page( filter)
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


