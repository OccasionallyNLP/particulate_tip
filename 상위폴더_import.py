# 상위 폴더 추가
import os
import sys
# 절대 경로의 상위 dir 경로를 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('__file__'))))
