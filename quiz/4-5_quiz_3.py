"""
Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

예) 생성된 비밀번호 : nav51!
"""

# 내 풀이
site = "http://naver.com" 
site = site[7:12]
print(site) # naver

count_e = site.find('e')
print(count_e) # 3

print(site[:3] + str(count_e) + '!') # nav3!


# 강의 풀이
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
print(my_str) # naver.com

my_str = my_str[:my_str.index('.')] # 규칮 2, my_str[:5]와 동일
print(my_str) # naver

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!' # 규칙 3
print(password) # nav51!

print("{0}의 비밀번호는 {1} 입니다.".format(url, password))