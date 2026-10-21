# 조건문, if (분기)
'''
if 조건:
   실행 명령문
'''

# weather = "맑아요"
weather = input("오늘 날씨는 어때요? ") # input, 사용자의 입력을 문자열 형태로 받음

if weather == "비" or weather == "눈":
  print("우산을 챙기세요.")
elif  weather == "미세먼지":
  print("마스크를 챙기세요.")
else:
  print("준비물 필요 없어요.") # 모든 조건이 맞지 않을 때 출력됨

# - - - - - - - - - - -

temp = int(input("기온은 어때요? ")) # 값을 정수 형태로 변경

if 30 <= temp:
  print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
  print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
  print("외투를 챙기세요.")
else:
  print("너무 추워요. 나가지 마세요.")