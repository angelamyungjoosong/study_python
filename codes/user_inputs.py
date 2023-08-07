# 파이썬에서 외부콘솔에서 받아올때 사용하는 것 - 스캐너 (타입이 중요)
# 값을 넣어주세요하는 표시와 값을 받는게 input()하나에 묶여있음 
# input한 값을 변수로 받아내기 
# input("Enter Name: ")
# pass

username = input("Enter Name : ")
number = input("Enter Number: ")

# Enter Name : angela
# Enter Number: 10 
type(username)
# <class 'str'>
type(number)
# <class 'str'>
int(number)
10
# 스트링을 인트로 바꾸는 방법 (따로 타입캐스팅하는 방법)
number = int(number)  


number = int(input("Enter Number: "))
# 실제로는 전체를 싸서 캐스팅해줌 

pass


