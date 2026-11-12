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

# Selenium = 요소속성인식
# Pyautogui = 좌표인식(요소를 분석할 필요가 없음, 속도가 굉장히 빠름)

# 웹 페이지 접근
driver.get("https://naver.co.kr")
driver.get("https://google.co.kr")

# 웹 페이지 타이틀 출력
'''
테스트 결과를 기록할 때 사용
ex) GOOGLE_TC01_RESULT : Pass
'''
print(driver.title)

# 현재 웹 페이지의 URL 출력
'''
실패한 케이스에서 실패 지점으로 바로 이동할 수 있는 링크를 제공하여 현상 확인을 위해 사용 (+ 타임스탬프도 같이 제공)
ex_ GOOGLE_TC01_RESULT : Fail(https://google.com/)
'''
print(driver.current_url)

# 부가 기능
# 웹 페이지 새로고침
driver.refresh()

# 웹 페이지 뒤로가기
driver.back()

# 웹 페이지 앞으로 가기
driver.forward()
