# {}이거는 딕셔너리(자료타입)
# key,value로 넣으면 된다 


# 초기화 방법 
# 어떤 값에 딕셔너리 넣고 싶으면 초기화 시킨 후에 할당시키자 
thisdict = {} #empty initial
thisdict = dict() #empty initial
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# value 부분에는 hashmap, list, string, int, 자기자신 dictionary 다 들어갈 수 있다

# # 1차적인 length 확인 (레코드의 갯수)
# len(thisdict)
# # 3

# # type 확인
# type(thisdict)
# # <class 'dict'>

# # 값을 가지고 오는 방법 
# thisdict['model']
# # 'Mustang'

# # 값을 변경하는 방법(자바 put와 비슷, key선택해서 value 넣어줌)
# thisdict['brand'] = "Yojulab"


# # key만 뽑아내기
# thisdict.keys()
# # dict_keys(['brand', 'model', 'year'])
# # 리스트([]보고 리스트임을 확인)

# type(thisdict.keys())
# # <class 'dict_keys'>
# # 타입확인했을때 이렇게 나오기 때문에 리스트로 타입캐스팅 후 사용 

# # value만 뽑아내기 
# thisdict.values()
# # dict_values(['Yojulab', 'Mustang', 1964])






# dictionary를 포문으로 돌리기 (기존에는 리스트만 포문을 넣을 수 있었음)

# for item in thisdict:
#     pass
 
#list를 enumerator과 비슷하게 작동한 것과 동일한 현상 / items쓰면 key와 value를 듀플 형식으로 나온다 
dict_format = "key : {0}, value : {1}"
# dict_format은 string이라는 형태가 됨 
for key, value in thisdict.items():
    print(dict_format.format(key, value))
    pass 
pass
# key : brand, value : Ford
# key : model, value : Mustang
# key : year, value : 1964

# 0,1 위치 바꾸어야
# dict_format = "key : {1}, value : {0}"
# for key, value in thisdict.items():
#     print(dict_format.format(value, key))
# pass 


# hashmap에서는 put이었지만  여기서는 key지정하고 값 할당 


# add item in dict(없는 key였으면 add, 있는 거였으면 수정됨)
thisdict['color'] = 'Red' 

# remove item in dict (key를 꼭 지정해줘야지 아니면 다 지워질수도 있다)
del thisdict['year']