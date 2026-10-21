# 반복문, for

# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

for waiting_no in range(1, 6): # 1 ~ 6 미만까지
  print("대기번호: {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
  print("{}, 커피가 준비되었습니다.".format(customer))

# - - - - - - - - - - -

# 반복문, while

# 예를 들어, 5번 불렀는데도 음료를 수령하지 않으면 음료를 폐기한다고 가정하자.

customer = "토르"
index = 5
while index >= 1:
  print("{0}님, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
  index -= 1
  if index == 0:
    print("커피는 폐기처분 되었습니다.")

# 무한 루프
customer2 = "아이언맨"
index = 1
while True:
  print("{0}님, 커피가 준비 되었습니다. 호출 {1}회.".format(customer2, index))
  index += 1

# 조건에 맞을 때까지 반복
customer = "토르"
person = "Unknown"
while person != customer:
  print("{0}님, 커피가 준비 되었습니다.".format(customer))
  person = input("이름이 어떻게 되세요? ")