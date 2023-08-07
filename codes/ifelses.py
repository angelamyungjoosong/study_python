first = 3
second = 4

# 기본 if-elif-else문
if (first < second) : 
    print('less first')
elif (first == second) : 
    print('equal')
else : 
    print ('great second')

# 컨디션으로 넣는건지 계산을 해서 넣는건지 구분을 하기 위해 
# 습관적으로 컨디션을 (fist < second) 괄호 묶는 방식으로 하자 
# else 다음에도 : 넣자 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# 루핑 돌릴때 break 사용해서 중간에 튀어나오게 하기 (orange일때)

for fruit in thislist:
    pass
    print(fruit)
    if (fruit == 'orange'):
        break
    # orange까지 나오게 

for fruit in thislist:
    pass
    if (fruit == 'orange'):
        break
    print(fruit)
    #cherry까지 나오게 

