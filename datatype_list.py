# list는 string과 비슷 
# string은 하나의 글자가 하나의 공간
# list는 하나의 공간이 여러개의 값 품고 있고 순서가 있어 (순열방식) (index형식)
# 글자가 하나의 문자가 된 셈 

#slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# 특정한 역할 가진  method가지고 있는것임 
pass 
# 변수 타입 궁금할때
type(thislist)
# <class 'list'>

# slicing은 index 번호를 기준으로 함 

# 순열방식 (string, list)는 length확인 가능 
len(thislist)
# 7

# String도 묶음이어서 list에 넣을수있음 (마치 Hashmap을 list에 넣었듯)
# list에서는 뒷부분은 -1이 적용(밑에서 오렌지는 안나옴)
thislist[1:3]   
# ['banana', 'cherry']



# 뒤에서부터 갈때는 string과 같이 -1적용 안됨 
thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

# change value in list  (특정한 값을 change) 두번째 것의 값을 바꿈 
# 인덱스가 어딘지, length도 알수 있다 
thislist[1] = 'watermelon'

# 두개의순서를 바꾼다 cherry와 watermelon
thislist[1:3] = ['cherry', 'watermelon']
# 갯수에 맞게 넣어주면 됨. 
# 시각화나 특정연산을 할때..특정항목을 넣을때 desc asc을 list로 넣음 


# sort 정렬 
# 알파벳 순으로 정렬 quick sort 왠만한것은 다 이 방식을 취한다 
thislist.sort() 

# 뒤에서부터 sort 
thislist.sort(reverse=True)


# 해쉬맵이 파이썬에서는 딕셔너리 
# 변수의 영역을 탭으로 구분 
# 리스트에서는 대괄호의 슬라이싱 방법 이해하기 

# 붙여넣기 (리스트에 추가하기)
thislist = ["apple", "banana", "cherry"]
thislist.append('melon')
thislist.append('orange')

# 값을 없애는 방법 (끝에 있는 게 없어짐)
thislist.pop()
#'orange'

# 초기화방식 
# empty  초기화 (값이 지정된(있는) 상태에서 값을 세팅해서 초기화)
thislist = []

# 권장되는 empty 초기화 (값이 없을 때/ 모를때는 이거 사용)
thislist = list()
# 자바에서 List thislist = new List();와 같은 문법. 인스턴스화시키는것. 


# 이런식으로 데이터타입 확인해야함 
type(thislist)
# <class 'list'>

# python casting: object로 선언하고 나서 다른 변수타입으로 형변환하기 위해 사용 
words = str()

#list에서 가장 많이 사용하는 문법이 for문 (리스트를 다 빼내기 위해)

pass

