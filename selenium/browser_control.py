# 드라이버 설정
import time
from selenium import webdriver

driver = webdriver.Chrome()

# 브라우저 창 최대화, 최소화
driver.maximize_window()
driver.minimize_window()
