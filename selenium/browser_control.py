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

'''
최대화를 사용하지 않고, 브라우저의 위치와 크기를 지정하는 이유

1. 사용자 환경마다 모니터의 해상도, 크기가 다름
2. 사용자 환경마다 모니터의 개수가 다름
3. 이런 이유로 사용자 환경마다 브라우저의 위치가 달라짐
4. 좌표를 기준으로 작성한 자동화 테스트는 실행 불가

브라우저의 위치와 크기를 지정하면 위의 문제들이 해결됨
똑같은 환경, 똑같은 모니터에서 계속 혼자 진행하지 않는 이상, 지정해줘야 함
'''
