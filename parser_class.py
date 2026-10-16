import time
import selenium
import os
import random
from PIL import Image , ImageEnhance
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Parser():
    def __init__(self, byfly_link , captcha_solve_link , login , password, listOurInformation):
        self.byfly_link = byfly_link
        self.captcha_solve_link = captcha_solve_link
        self.login = login
        self.password = password
        self.listOutInformation = listOurInformation

   
    def byflyRegistration(self):
        driver = webdriver.Chrome(options=self.changeCurrentCountry())
        driver.get(self.byfly_link)


        login_input = driver.find_element(By.ID, self.listOutInformation[0])
        login_input.clear()
        login_input.send_keys(self.login)
        time.sleep(random.uniform(1.0 , 5.0))


        password_input = driver.find_element(By.NAME , self.listOutInformation[1])
        password_input.clear()
        password_input.send_keys(self.password)
        time.sleep(random.uniform(1.0 , 5.0))

        captcha_image = driver.find_element(By.ID , self.listOutInformation[2])
        captcha_image.screenshot('screenshots/captcha.png')

        captcha_text_input = driver.find_element(By.ID , self.listOutInformation[3])
        captcha_text_input.clear()
        self.changeCaptchaImage() 
        captcha_text_input.send_keys(self.getCaptchaText())
        time.sleep(random.uniform(1.0 , 5.0))

        enter_button = driver.find_element(By.CSS_SELECTOR , self.listOutInformation[4])
        enter_button.click()

        input()

    def changeCaptchaImage(self):
        image = Image.open('screenshots/captcha.png')

        if image.mode != "RGB":
            image = image.convert("RGB")

        brightness_factor = 1.2
        enhancer_b = ImageEnhance.Brightness(image)
        bright_img = enhancer_b.enhance(brightness_factor)

        contrast_factor = 1.5
        enhancer_c = ImageEnhance.Contrast(bright_img)
        final_img = enhancer_c.enhance(contrast_factor)

        final_img = final_img.convert('1')
        final_img.save("screenshots/result_captcha.png")

        os.remove('screenshots/captcha.png')
        
    def getCaptchaText(self):
        driver = webdriver.Chrome()
        driver.get(self.captcha_solve_link)
        wait = WebDriverWait(driver, 10)

        path_captcha = os.path.abspath('screenshots/result_captcha.png')
        image_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        image_input.send_keys(path_captcha)
        time.sleep(random.uniform(1.0 , 5.0))
        os.remove('screenshots/result_captcha.png')

        extrude_text = driver.find_element(By.CSS_SELECTOR , "div[style='pointer-events: auto;']")
        extrude_text.click()
        time.sleep(5)

        result_captcha_text = driver.find_element(By.ID , 'result__text0').text
        return result_captcha_text

    def changeCurrentCountry(self):
        options = Options()
        new_user_agent = f'Mozilla/5.0 (Windows NT {random.randint(1, 1_000)}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36'
        options.add_argument(f"--user-agent={new_user_agent}")
        options.add_argument(f'--proxy-server=https://124.105.180.29')
        return options
        



    def __del__(self):
        print('Program succefuly finished')
    