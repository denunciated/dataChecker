import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class GoogleCheckerTest(unittest.TestCase):
    def setUp(self):
        # Set up the Selenium WebDriver (using Chrome as an example)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

    def test_username_denunciated(self):
        self.driver.get('https://github.com/denunciated')
        username_span = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[itemprop="additionalName"]'))
        )
        self.assertEqual(username_span.text.strip(), 'denunciated')
        
    def test_user_has_recent_commits(self):
        self.driver.get('https://github.com/denunciated')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'td.ContributionCalendar-day'))
        )
        tds = self.driver.find_elements(By.CSS_SELECTOR, 'td.ContributionCalendar-day')
        today = datetime.now().date()
        week_ago = today - timedelta(days=7)
        recent_commit_found = False

        for td in tds:
            data_date = td.get_attribute('data-date')
            data_level = td.get_attribute('data-level')
            if data_date and data_level:
                date_obj = datetime.strptime(data_date, '%Y-%m-%d').date()
                if week_ago <= date_obj <= today and int(data_level) >= 1:
                    recent_commit_found = True
                    break

        self.assertTrue(recent_commit_found, "No recent commits found in the last 7 days.")


if __name__ == '__main__':
    unittest.main()

