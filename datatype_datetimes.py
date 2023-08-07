import datetime 

# 오늘 날짜 (print today)
today = datetime.datetime.now()
# pakcage.class.method


# today
# datetime.datetime(2023, 8, 4, 18, 14, 7, 800525)
# 변수에 각각 담겨있다(셋팅된 값이 int형으로 들어있다)


# type(today)
# <class 'datetime.datetime'>

someday = datetime.datetime(2023, 8, 3)
# 넣은 값을 그대로 셋팅하고 있다 



# 오늘날짜 - 특정 날짜 
# datetime은 년,월,일,시 등 표시를 위해서 사용 (형식) 하는 function 
# 시작일은 1970년 / 년,월,일만 기본셋팅으로 넣어주면 된다 
someday - today
# datetime.timedelta(days=-5, seconds=50475, microseconds=906294)
# special variables
# function variables
# days:
# -5
# max:
# datetime.timedelta(days=999999999, seconds=86399, microseconds=999999)
# microseconds:
# 906294
# min:
# datetime.timedelta(days=-999999999)
# resolution:
# datetime.timedelta(microseconds=1)
# seconds:
# 50475


# 분 초 써주지 않으면 0으로 셋팅됨 
datetime.datetime(2021, 2, 2)
# datetime.datetime(2021, 2, 2, 0, 0)

# 하루를 나타내는 초로 나눔 ? 
50578/(24*60*60)
# 0.5853935185185185

somedelta = someday - today 

type(somedelta)
# <class 'datetime.timedelta'>

somedelta.days
# -5

# quest 
# -2023.5.8부터 오늘까지 흐른 day 
maytoday = datetime.datetime(2023, 5, 8)
maysomeday = datetime.datetime.now()
maydelta = maysomeday - maytoday
maydelta.days
# 91
pass

