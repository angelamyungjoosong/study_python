# def mlmodel(data:dict) : 
#     print('data with dict {}'.format(data))
#     return data

# result = mlmodel({'msg':'hello !'})
# print('result : {}'.format(result))




# with machine learning model   # function에서 dictionary로 받는 것으로 달라진다 # 데이터 넣어주고 나서 분해 
# {'texture_mean':16.34, 'perimeter_mean':87.21}-> data
import pickle

def mlmodelwithregression(data:dict) :  #data가 dict로 대치 
    print('data with dict {}'.format(data))

    # data dict to 변수 할당 
    texture_mean = data['texture_mean']
    perimeter_mean = data['perimeter_mean']

    #pkl 파일 존재 확인 코드 필요

    result_predict = 0
    # 학습 모델 불러와 예측 
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict)) #array(차원이 있는것)으로 리턴, 딕셔너리 리턴이 더 좋음(여러값을 넣을 수 있게)
        pass

    #예측값 리턴 
    result = {'radius_mean': result_predict[0]}
    return result #리턴은 묶음으로 하는 게 좋음 

# 예제 [[16.34, 87.21]]
result = mlmodelwithregression({'texture_mean':16.34, 'perimeter_mean':87.21})
print('result : {}'.format(result))