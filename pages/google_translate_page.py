import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleTranslatePage:
    def __init__(self, sb_driver):
        self.sb = sb_driver
        self.driver = sb_driver.driver

    def open(self, url="https://translate.google.com/?sl=auto&tl=fr&op=docs"):
        self.sb.open(url)
        time.sleep(random.randint(5, 8))

    def upload_file(self, file_path):
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(file_path)
        time.sleep(random.randint(3, 6))

    def translate_and_download(self):
        for count in range(1, 11):
            try:
                btn = self.driver.execute_script(
                    'return document.querySelector("#yDmH0d > c-wiz > div > div.ToWKne > c-wiz > div.R5HjH > c-wiz > div.oLbzv > c-wiz > div > div:nth-child(1) > div > div.ld4Jde > div > div > button")')
                self.driver.execute_script("arguments[0].click();", btn)

                # Wait for download button
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//span[text()='Download translation']/.. | //span[text()='Télécharger la traduction']/..")
                    )
                ).click()
                return True
            except:
                self.driver.execute_script("arguments[0].click();", btn)
                print("Processing ...")
                if count == 10:
                    return False
