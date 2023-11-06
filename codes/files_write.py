# 특정한 곳에 파일을 저장하고 불러오는 방법 
# with는 try catch문과 비슷, 예외 조건을 처리 
# with open(파일 이름, 파일을 여는 목적(r, w))
# as --는 우리가 줄 수 있는 변수의 값 with 내 쓰는 알리아스 
data = "write somethings"

with open('temp_file.txt', 'w') as fw :
    fw.write(data) 
    # 글자를 파일에 넣어 

pass 



