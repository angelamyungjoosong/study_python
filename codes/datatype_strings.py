string = "Yojulab !"
len(string) 
pass 

# 프린트없이 코드가 동작되는걸 보기 위해 pass 사용

# len(string)
# 9
# "ju" in string 
# True
# "Not" in string
# False
# "Not" not in string
# True

# https://www.w3schools.com/python/default.asp

# slicing 말그대로 잘라내는 기능   
string[3] 
pass 

string[3]
# 'u'       0부터 시작해서 4번쨰 

string[3:6]   
# 순열 방식 = series (index와 값이 같이 들어가있는 방식)
# 'ula'      from 3 to 6  4번째부터 7번째까지

string[3:]
# 'ulab !'     4번째부터 끝까지 

string[:-2]
# Yojulab'   전체에서 특정값을 자동으로 자르고 싶을때 


# 스트링 format  넣어줄때 타입이 선언됨 / 타입이 다른 두 변수를 concat합칠때만 이런 에러 일어남
age = 36
txt = "My name is John, I am " + str(age)
print(txt)


#  {}는 변수의 값을 대치. 보통은 string인데 format을 붙여주면 변수가 대치됨. 
txt_second = "My name is John, I am {}."
txt_second 
'My name is John, I am {}.'

# 인스턴스화를 하면서 메소드를 끌어안고 있는데 그중에 format을 사용.
# 변수 age를 순서에 입각해서 넣어줌.  포문을 돌릴때 특정 위치에 변수로 값을 줘서 돌릴때 유용 
# format에서는 cascade 안해도 됨 
txt_second.format(age)
'My name is John, I am 36.'

quantity = 3  # index 0
itemno = 567  # index 1
price = 49.95 # index 2
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just {2}."

# 변수는 세개, 표현해야하는 값은 네개. 순서를 적용
# 순서적으로 쓸려고 함. 재사용. 번호 넣는 방법을 취함
myorder.format(quantity, itemno, price)
'I want 3 pieces of item 567 for 49.95 dollars. I have just 49.95.'

pass









