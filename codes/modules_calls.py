# modules.py에 있는 것을 호출할 때 사용 

# modules에 function선언하고 
# 사용은 modules_calls
# 파일 분리가 되었기 때문에 연관성이 필요 -> import가 필요 

# 기존자바에서는 파일 안의 class를 import했었음. class이름이 파일이름과 동일하게 맞춰줬었음
# 파일이름과 class는 동급이다 / 그 안에 method의 집합 

# class를 만들지는 않지만 function을 modules로 묶고 있다고 볼 수 있음 

import modules 
# 모듈스를 호출
# 파일이름과 동일(모듈)

# modules. (modules안의 부분가져오는 것과 동일, 자바의 클래스와비슷)
# modules로 가서 있다는 것을 인증하고 다시 돌아와... 
result_sum = modules.add(8, 1)

# call한 위치가 global (디버깅 시작한곳)

# import할때 alias를 줌. 
# 파이썬에서 import는 인스턴스화되는 것과마찬가지(자바는 import후인스턴스도 해야함)
# 만약 그 안의 function이 많은 경우는 내부에서 짧게 쓴다. 

#alias 
import modules as mdls 
result_sum = mdls.multiply(8,1)



from modules import person1 as ps
print(ps['country'])

pass


# 모듈스 안에 두가지 성격이 같이 있을때 
# function / dictionary(object로 인식(object와 class를 동급으로 여김))
# 그럴경우 dictionary는 독립적인 class이다 
# class의 어느것인지 (한번더 들어가야하는상태)
# 이럴때는 person1을 클래스로 생각하기 
# 한단계 더 들어가기 위해 쓰는 방법 -> from
# 파일 내에 밖으로 나와있는 function이 아니고 랩핑된 function이나 modules가 있을때 사용 
# person1 안에 country 
# 클래스가 또 들어있거나 딕셔너리 있을때 다시 안으로 들어가야할때 사용 
