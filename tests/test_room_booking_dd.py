import datetime
import logging
import os
import time
from pages.basePage import BasePage
from pages.page_home import HomePage
from utils.excel_utils import *


def test_room_cost(setup):
    # Get the current working directory dynamically
    base_dir = os.getcwd()
    # Construct the file path dynamically
    file_path = os.path.join(base_dir, "data", "test_data2.xlsx")
    sheet_name = "Sheet1"

    # Read test data as a list of dictionaries
    test_data = read_test_data(file_path, sheet_name)
    for index, data in enumerate(test_data, start=2):  # starting at row 2 in the sheet
        (room_type, start_month, start_day, start_year, start_hour, start_minute, start_time,
         end_month, end_day, end_year, end_hour, end_minute, end_time, expected_cost) = data

        base_page = BasePage(setup)  # Adjust based on your actual setup
        base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

        home_page = HomePage(setup)
        home_page.select_room(room_type)
        home_page.set_start_time(start_month, start_day, start_year, start_hour, start_minute, start_time)
        home_page.set_end_time(end_month, end_day, end_year, end_hour, end_minute, end_time)
        home_page.click_room_book_button()

        # Get the actual cost from the web page
        actual_cost = home_page.get_actual_booking_cost()

        # Compare expected cost with actual cost and determine test result
        result = "Passed" if actual_cost == expected_cost else "Failed"

        # Write the actual cost to column 14 (Actual Cost) and the result to column 15 (Result)
        write_test_data(file_path, sheet_name, index, 14, actual_cost)
        write_test_data(file_path, sheet_name, index, 16, result)

    print("Test execution completed and results written to Excel.")