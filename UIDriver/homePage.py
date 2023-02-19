from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#  the below code will keep the window open after automation is done
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://lyricninja-env-1.eba-hq4sm8mv.us-east-2.elasticbeanstalk.com/")
# driver.close()
# driver.quit()

from selenium.webdriver.common.by import By

class GameBase:
    def __init__(self, driver):
        self.driver = driver
        
# need to adjust the ids and classes in the original project to make selecting a little easier
    center = driver.find_element(By.CLASS_NAME, "center")
    anchor_tags = center.find_elements(By.TAG_NAME, "a")
    playButton = anchor_tags[1]
    playButton.click()




