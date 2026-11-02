# 함수
'''
함수 정의
def 함수이름():
'''

# 함수 정의
def open_account():
  print("새로운 계좌가 생성되었습니다.")

# 함수 호출
open_account()

# - - - - - - - - - - - - - - - - - - - - 

# 전달값과 반환값

# 입금하는 상황
def deposit(balance, money):
  print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))

  # 값 반환
  return balance + money

balance = 0 # 잔액 0원
balance = deposit(balance, 1000)
print(balance) # 1000

# 출금하는 상황
def withdraw(balance, money):
  if balance >= money: # 잔액이 출금보다 많으면
    print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
    return balance - money
  else:
    print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
    return balance

balance = 0
balance = deposit(balance, 1000) # 현재 잔액 1000원
balance = withdraw(balance, 2000) # 출금 안됨
balance = withdraw(balance, 500) # 출금 됨, 잔액 500원

# 저녁에 출금(수수료 있는 경우)
def withdraw_night(balance, money):
  commission = 100 # 수수료 100원
  return commission, balance - money - commission # 튜플 형식

balance = 0
balance = deposit(balance, 1000) # 잔액 1000원
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance)) # 수수료 100원, 잔액 400원