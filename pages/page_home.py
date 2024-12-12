from pages.basePage import BasePage
from locators.homePageLocators import HomePageLocators
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def select_room(self, value):
        self.select_dropdown_option_by_value(*HomePageLocators.Select_room, value)

    def set_start_time(self, day, month, year, hour, minute, am_pm=None):
        """
        Sets the start time by interacting with the datetime-local input field.

        :param day: The day to set (e.g., "12").
        :param month: The month to set (e.g., "12").
        :param year: The year to set (e.g., "2024").
        :param hour: The hour to set (e.g., "12").
        :param minute: The minute to set (e.g., "30").
        :param am_pm: Optional. AM/PM format ("AM" or "PM"). If not provided, 24-hour time will be used.
        """
        # Ensure that month, day, hour, and minute are zero-padded if necessary
        month = month.zfill(2)
        day = day.zfill(2)
        hour = int(hour)  # Convert hour to integer for further processing
        minute = minute.zfill(2)  # Ensure two digits for minute

        # Handle AM/PM logic
        if am_pm:
            if am_pm.upper() == "AM" and hour == 12:
                hour = 0  # Midnight (12 AM) should be 00 in 24-hour format
            elif am_pm.upper() == "PM" and hour != 12:
                hour += 12  # Add 12 to convert PM to 24-hour format (1 PM -> 13)

        # Format the date-time string to match 'yyyy-mm-ddTHH:mm' format (24-hour time)
        hour = str(hour).zfill(2)  # Ensure the hour is two digits
        date_time_str = f"{month}-{day}-{year}T{hour}:{minute}"

        # Click on the start time input field to focus it
        self.click_element(*HomePageLocators.Start_time)

        # Clear any existing text (optional, but helpful in case of pre-filled values)
        self.driver.find_element(*HomePageLocators.Start_time).clear()

        # Send the formatted date-time string to the input field
        self.driver.find_element(*HomePageLocators.Start_time).send_keys(date_time_str)

    def set_end_time(self, day, month, year, hour, minute, am_pm=None):
        """
        Sets the start time by interacting with the datetime-local input field.

        :param day: The day to set (e.g., "12").
        :param month: The month to set (e.g., "12").
        :param year: The year to set (e.g., "2024").
        :param hour: The hour to set (e.g., "12").
        :param minute: The minute to set (e.g., "30").
        :param am_pm: Optional. AM/PM format ("AM" or "PM"). If not provided, 24-hour time will be used.
        """
        # Ensure that month, day, hour, and minute are zero-padded if necessary
        month = month.zfill(2)
        day = day.zfill(2)
        hour = int(hour)  # Convert hour to integer for further processing
        minute = minute.zfill(2)  # Ensure two digits for minute

        # Handle AM/PM logic
        if am_pm:
            if am_pm.upper() == "AM" and hour == 12:
                hour = 0  # Midnight (12 AM) should be 00 in 24-hour format
            elif am_pm.upper() == "PM" and hour != 12:
                hour += 12  # Add 12 to convert PM to 24-hour format (1 PM -> 13)

        # Format the date-time string to match 'yyyy-mm-ddTHH:mm' format (24-hour time)
        hour = str(hour).zfill(2)  # Ensure the hour is two digits
        date_time_str = f"{month}-{day}-{year}T{hour}:{minute}"

        # Click on the start time input field to focus it
        self.click_element(*HomePageLocators.End_time)

        # Clear any existing text (optional, but helpful in case of pre-filled values)
        self.driver.find_element(*HomePageLocators.End_time).clear()

        # Send the formatted date-time string to the input field
        self.driver.find_element(*HomePageLocators.End_time).send_keys(date_time_str)

    def click_room_book_button(self):
        self.click_element(*HomePageLocators.Book_room_button)

    def get_actual_booking_cost(self):
        return self.get_element_text(*HomePageLocators.Booking_cost)
