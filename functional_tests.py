"""Functional Test for Superlist App"""
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.BROWSER = webdriver.Firefox()

    def tearDown(self):
        self.BROWSER.quit()

    def test_can_start_a_new_list_and_retrieve_it(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.BROWSER.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        assert 'To-Do' in self.BROWSER.title, f"Browser title was {self.BROWSER.title}"

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a textbox inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders wheter the site will remember her list. Then she sees
        # that the site has generated a unique url for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
