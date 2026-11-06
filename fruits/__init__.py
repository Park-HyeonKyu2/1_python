# fruits/__init__.py
# 없어도 되나 있으면 패키지를 쓰는 사람이 영향을 받게 된다.
from .apple import info as apple_info, func1
from .banana import info as banana_info

# 예) import fruits
# 예) from fruit import apple_info, banana_info
# 예) from fruit import *
__all__ = ["apple_info", "banana_info", func1] # *(모든 것)을 불러올 때 __all__로 등록한 둘만 가져가게 된다.
