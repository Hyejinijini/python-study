# 드라이버 설정
import time
from selenium import webdriver

driver = webdriver.Chrome()

# 브라우저 창 최대화, 최소화
driver.maximize_window()
driver.minimize_window()

# 브라우저 위치 지정(지정된 좌표에 창이 열림)
driver.set_window_position(0, 0)

# 브라우저 크기 지정(지정된 사이즈로 창이 열림)
driver.set_window_size(1470, 956)

