import sys

option = sys.argv[1]

if option == "-a" :
    memo = sys.argv[2]
    f = open("memo.txt" , "a")
    f.write(memo)
    f.write("\n")
    f.close()
elif option == "-v":
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)

'''import sys 모듈사용 방법 for mac'''
# import sys가 입력되어 있는 파일이 위치한 디렉토리까지 이동
# ls로 파일목록 확인 후 python sys파일명을 입력 후 sys조건에 맞는 입력을 실행
