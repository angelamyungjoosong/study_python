# package == module(python)

# 값을 넣는다/할당된다하면 그건 class라고 생각하면 된다, 그안에 function 있다 

# 일반 변수는 datatype지정 안한다 / 하지만 function에는 def(선언) 할당한다 -  얘는 function으로 선언할거라는 표시 
# function은 def 쓰고 function이름 쓰고 그 뒤에 (), 여기부터가 영역이라는 표시의 : 와 tab 
# 데이터타입이 없으니까 리턴 타입은 들어가지 않는다/ 만든 사람이 인지만 하고 있으면 됨. 

# <기본 function 구성>
def function_name() :
    pass
    return 0

# function호출  
function_name()
pass 

# 은폐방식(안의 내용은 알필요없고 들어오고 나오는거만 중요)
# 밑에서 호출하면 call하니까 다시 function 안으로 들어간다 

print(function_name())
# 0
# 0이 리턴되어 출력됨 







# 평범한 params 이용한 결과값 받기 <합산 function> 
# function에 parameter두개 넣어 합산해서 리턴해서 사용하려고함 
def add(first, second):
   sum = first + second
   return sum
# first,second라는 변수로 넣어줌

# 변수가 아닌 상수로 넣어줌 
result_sum = add(4,6)
pass

# 리턴값을 사용하지 않으면 호출만 하고 할당안함  
# 리턴값 활용하려면  =을 사용해서 변수 사용 

# function def되어있는 것 인지 -> resultsum에는 10이 들어가있을 것임 

# 한쪽이 없게  call하는 경우도 있다 
# add(1)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# TypeError: add() missing 1 required positional argument: 'second'
# argumet = parameter 







# set default value with params (param에 default 주는 것)
# 한쪽만 넣었을때 다른것은 (값이 들어가지 않았을때) 디폴트로 셋팅이 되어있게 만들기 
def minus(first, second=0):
    result = first - second 
    return result

minus(3, 5)
minus(3)







# 묶음 리턴 (hashmap이나 list나 방식 말고 머신러닝에서 여러개 변수를 한꺼번에 리턴하는 방식)
# (듀플을 통해 데이터를 묶어서 던져서 받을 수 있다)
# dict_format = "key : {0}, value : {1}"
# # dict_format은 string이라는 형태가 됨 
# for key, value in thisdict.items():
#     print(dict_format.format(key, value))
#     pass 
# pass
# 여기서처럼 듀플 안의 값을 따로따로 받아낼 수 있다 

# {}는 dictionary
# []는 리스트 
# ()는 듀플 

# 내가 넣어준 세개의 변수를 모두 사용해서 리턴을 받을 것임
# 듀플로 변수 여러개를 묶어서 보냄. 듀플도 하나의 변수니까. 
# 하나 넣어도 작동할 수 있게 second=1
# (multiply, first, second)는 하나의 묶여있는 변수 

#return tuple datatype
def multiply(first, second=1):
    multiply = first * second
    # like list (multiply, first, second)는 위에 있는 것과 동일 
    return (multiply, first, second)

result_tuple = multiply(3, 4)
multiply, first, second = multiply(4)
_, result_multiply, result_first = multiply(4)

# (multiply, first, second) = multiply(4)와 같음. 이렇게 여러개를 쓸 때는 듀플이라고 생각하면 됨. 
# 할당되는 값 있고 = 이후 변수 여러개 있으면 듀플임. return의 순서와 같게 써야함 

# result_multiply
# (12, 3, 4)
# type(result_multiply)
# <class 'tuple'>
# 묶인 걸 쪼개기 
# 해당부분에 변수를 사용하지 않을때 _사용. 순서 및 개수 맞춰야할때. _도 변수다 
# 특정 변수를 function 내부에서 사용할때 

pass
