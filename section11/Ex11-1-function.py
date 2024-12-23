'''
파일명: Ex11-1-function.py

함수 (function)
    특정 작업을 수행하기 위해 독립적으로 설계된 코드블록
    입력값을 받아서 처리한 후, 결과를 반환하거나, 반환없이 작업을 수행할 수 있다.

  힘수 정희 형식:

  def 함수이름(매개변수):
    수행할 코드
    return 반환값

'''

#welcome()함수 정의(실행하지 않음)
def welcome(): #매개변수 없음, 리턴값 없음 ==> 입력값 없이 실행 후 끝나는 함수
    print('Hello, Python')
    print('Nice to meet you!')

print('프로그램 시작!')
welcome()#함수 호출
print('프로그램 종료!')