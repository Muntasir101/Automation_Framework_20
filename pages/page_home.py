from pages.basePage import BasePage
from locators.homePageLocators import HomePageLocators


class HomePage(BasePage):
    def select_room(self):
        self.select_dropdown_option_by_value(*HomePageLocators.Select_room)

    def set_start_time(self):
        self.click_element(*HomePageLocators.Start_time)

    def set_end_time(self):
        self.click_element(*HomePageLocators.End_time)

    def click_room_book_button(self):
        self.click_element(*HomePageLocators.Book_room_button)
