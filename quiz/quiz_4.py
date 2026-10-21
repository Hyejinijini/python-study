'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
1st = [1,2,3,4,5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))

# shuffle, 리스트 안의 값을 무작위로 변경함
# sample, 리스트에서 랜덤으로 숫자를 뽑음
'''

# 내가 푼 풀이
from random import *

user_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # 조건 1, 아이디 1~20개의 리스트
shuffle(user_id) # 조건 3, random 모듈의 shuffle 사용

chicken = sample(user_id, 1) # 조건 2, 무작위 당첨자 추첨
remaining = list(set(user_id) - set(chicken)) # chicken 당첨자 제외
coffee = sample(remaining, 3) # 조건 2, 무작위 당첨자 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(chicken[0]))
print("커피 당첨자 : {}".format(coffee))
print("-- 축하합니다 --")



# 강의 풀이
from random import *

users = range(1, 21) # 조건 1, 1~20까지 숫자를 생성
users = list(users) # range 타입을 list 타입으로 변경

shuffle(users) # 조건 3, random 모듈의 shuffle 사용

winners = sample(users, 4) # 조건 2, 무작위로 당첨자 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")