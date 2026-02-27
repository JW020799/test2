#sys 모듈:파이썬에서 제공하는 라이브러리 모듈 
import sys

print(sys) 
print(sys.path)

sys.path.append('c:/unit')
print(sys.path)
print(type(sys.path))

import test
print(test,add(1,2))