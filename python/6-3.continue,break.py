'''
둘 다 반복문 내에서 사용 가능

1) Countinue : 해당 반복은 건너뛰기
2) Break : 반복문 끝내기
'''

# 결석한 학생들은 넘어가고 나머지 학생들만 책을 읽게 하자.
absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴

for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
  if student in absent: # [2, 5]가 포함되어 있다면 countinue, 건너뛰기
    continue
  elif student in no_book: # [7]이 포함되어 있다면 반복문 끝내기
    print("오늘 수업은 여기까지. {0}, 교무실로 따라와.".format(student))
    break
  print("{0}, 책을 읽어봐")