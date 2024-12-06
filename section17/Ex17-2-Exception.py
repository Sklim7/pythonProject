'''
파일명: Ex17-2-Exception.py

'''

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print(f'발생 예외 메세지{e}')