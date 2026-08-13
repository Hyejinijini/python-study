# 탈출 문자

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
'''
백문이 불여일견
백견이 불여일타
'''

# 문자열 내에 따옴표 사용
# 따옴표 다르게 해서 사용
print("저는 '공주'입니다.")
print('저는 "공주"입니다.')

# \" \' : 문장 내에서 따옴표
print("저는 \"공주\"입니다.") # 큰 따옴표 앞에 역슬래쉬(\) 입력 시, 문장 내에서 따옴표를 출력해주는 역할 = 탈출 문자

# \\ : 문장 내에서 \ 출력
print("\\") # \

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Red \bApple") # RedApple

#\t : 탭(Tab)
print("Red\tApple") # Red      Apple