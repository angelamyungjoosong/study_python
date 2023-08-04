thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

 #for 내부값 in list 
# for item in items: 
#     pass 

for item in thislist:
    print(item)

# apple
# banana
# cherry
# orange
# kiwi
# melon
# mango

#포문은 리스트형식으로 되어있어야한다 
# item 대신 fruit 사용 가능 

for fruit in thislist:
    print(fruit)

# 뭉쳐있는거 일때 
pass
range(2, 10)
# start:
# 2
# step:
# 1
# stop:
# 10
# 2부터 10까지 1씩
# for (int i=2; i < 10; i++) { //java
#     print(i)
# }

# 뭉쳐있는게 리스트면 위에꺼, 인덱스 번호로 사용하겠다하면 밑에꺼  (두개 합치는 것도 가능)
for i in range(2,10): #python for
    print(i)

# while  (문법 규칙이 while, condition, 영역 이런 패턴으로 간다)
first = 3 
while (first < 6) :
    pass
    print('while count {}'.format(first))
    first = first + 1
# while count 3
# while count 4
# while count 5


# list with numbering (list + numbering 같이 할 수 있는 것)
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits)

# fruits_enu 변수에 담기- 값이 안보임/i:9 이라고 부여됨/ 데이터 베이스에 request 던지고 떨어지는 resultset..while문을 돌리면서 next넣어준거처럼 한 레코드씩 가져와.
# 순서적으로 넣어줌. 그래서 next를 넣어줘어야 동작함 
# 리스트 (순서적으로 되어있는 것)을 데이터베이스와 유사한거로 바꿔줌 (번호가 넘버링됨)
# 시각화할때 많이사용. x축있고 y축 만들때 사용 
# hashmap 넣어주면 hashmap 나오고 list넣어주면 list 나옴 (리스트는 []로 싸줌)

# enumerate 원리 이해 
next(fruits_enumerate)
# (0, 'apple')
next(fruits_enumerate)
# (1, 'banana')
next(fruits_enumerate)
# (2, 'cherry')
next(fruits_enumerate)
# (4, 'kiwi')
next(fruits_enumerate)
# (5, 'melon')
next(fruits_enumerate)
next(fruits_enumerate)
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# StopIteration 값이 없으면 false로 떨어져. -> for문으로 사용 가능 (next로 계속 회전시키는 느낌)

# (0, 'apple') 이걸 듀플이라함. 앞에는 인덱스, 뒤에는 실제 들어갔던 값. 듀플도 리스트와 비슷. 리스트에 묶여있는 값. 한번 세팅되면 n변화될 수 없는 값. 
# 분리되어있는 데이터를 한번 사용하기 위해서 묶어주는 셋팅. 묶음 장치. 분리되지 않지만 방법은 있다. 

# list with numbering (for문 내에서 듀플 사용 방법)
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits) 
# 듀플이라는 형식으로 묶여있는 상태 

# 안보이다가 포문을 사용하면 next를 내부적으로 돌리면서 하나씩던져줄것임
# 그냥 찍으면 듀플로 찍힘
# 듀플 묶음
for index_fruit in fruits_enumerate:
    print(index_fruit)
    pass
pass
# (0, 'apple')
# (1, 'banana')
# (2, 'cherry')
# (3, 'orange')
# (4, 'kiwi')
# (5, 'melon')
# (6, 'mango')


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_enumerate = enumerate(fruits) 
# 앞에 있는 것, 뒤에 있는 것 따로 변수로 지정해서 내부의것을 분리해서 사용가능 
# 듀플 분리 (앞을 index, 뒤를 fruit 변수로)
fruit_print_format = "number: {0}, fruit name:{1}"
# 0,1 나중에 포멧에 넣어줄 순서 
# 브레이스 넣는  이유는 스트링 포멧을 넣기 위해서 
# {}을 변수로 채울것임 
# 스트링과 enumrate합쳐서 프린트 
for (index, fruit) in fruits_enumerate:
    print(fruit_print_format.format(index, fruit))
    pass
pass
# number: 0, fruit name:apple
# number: 1, fruit name:banana
# number: 2, fruit name:cherry
# number: 3, fruit name:orange
# number: 4, fruit name:kiwi
# number: 5, fruit name:melon
# number: 6, fruit name:mango

