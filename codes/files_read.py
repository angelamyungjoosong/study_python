# 파일 존재 확인 후 
import os 

file_path = 'codes/temp_file.txt'

if os.path.exists(file_path) :# 존재 여부 return이 True/False 
    # 파일 관련 업무 실행 
    with open(file_path, 'r') as fr:
        pass
        load_file_read = fr.read()
        pass 
else:
    print("File does not exist")

# 파일 이름, 목적 순 