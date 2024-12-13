import datetime
import time

import openpyxl

from pages.basePage import BasePage
from pages.page_home import HomePage


def read_test_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data


def test_room_cost(setup):
    test_data = read_test_data("E:\\Offline_Batch_20\\Projects\\Automation_Framework_20\\data\\test_data.xlsx",
                               "Sheet1")
    for data in test_data:
        room_type, start_date, start_time, end_date, end_time = data

        start_month, start_day, start_year, = start_date.split("-")
        start_hour, start_minute, start_period = start_time.split(":")

        end_month, end_day, end_year = end_date.split("-")
        end_hour, end_minute, end_period = end_time.split(":")

        base_page = BasePage(setup)
        base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

        home_page = HomePage(setup)
        home_page.select_room(room_type)

        home_page.set_start_time(start_month, start_date, start_year, start_hour, start_minute, start_period)

        home_page.set_end_time( end_month, end_date, end_year, end_hour, end_minute, end_period)

        home_page.click_room_book_button()

        time.sleep(8)
