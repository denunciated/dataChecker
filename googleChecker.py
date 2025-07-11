from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleCheckerTest(unittest.TestCase):
    def setUp(self):
        # Set up the Selenium WebDriver (using Chrome as an example)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

    def test_google_homepage_title(self):
        # Example test: check Google homepage title
        self.driver.get('https://www.google.com')
        self.assertIn('Google', self.driver.title)
    
    def test_google_search_github(self):
        self.driver.get('https://www.google.com')
        searchbox = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea')
        searchbox.send_keys('github')
        searchbox.send_keys(Keys.ENTER)
        result_cite = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/div[2]/cite'))
        )
        self.assertEqual(result_cite.text, 'https://github.com')

if __name__ == '__main__':
    unittest.main()

