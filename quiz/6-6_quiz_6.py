'''
Quiz 6) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1: 승객별 운전 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

# 내 풀이
# 우선, random모듈을 불러옴 (난수), randint(5, 50)
# 50번을 반복하면서 5~15분 사이의 승객만 count해야함 > count 변수 생성, count = 0
# > 그럼 일단 반복문을 50번 돌려야함 > range 사용, range(1, 51)
# 반복문을 돌면서 난수가 matching에 포함된다면 print 구문 출력 후, count+=1
# 아니라면 count 되지 않고, print 구문만 출력
# 마지막에 총 탑승 승객 count 출력


from random import *

matching = list(range(5, 16))
count = 0

for customer in range(1, 51):
  time = randint(5, 50)

  if time in matching:
    print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
    count += 1
  else:
    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))

print("총 탑승 승객 : {0}분".format(count))

# - - - - - - - - - - - - - - - - - - - - - -

# 강의 풀이

from random import *

cnt = 0 # 총 탑승 승객 수

for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
  time = randrange(5, 51) # 5분 ~ 50분 소요 시간

  if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
    print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
    cnt += 1
  else: # 매칭 실패한 경우
    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(count))