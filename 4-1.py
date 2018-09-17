import pickle #객체 텍스트 직렬화, 역직렬화

# 파일 이름과 데이터

bfilename = 'c:/workspace/section4/test.bin'
tfilename = 'c:/workspace/section4/test.txt'

data1 = 77
data2 = 'hello'
data3 = ['car', 'apple']

#바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1,f) #dump()바이너리 // dumps(텍스트) 직렬화
    pickle.dump(data2,f) #dump()바이너리 // dumps(텍스트) 직렬화
    pickle.dump(data3,f) #dump()바이너리 // dumps(텍스트) 직렬화


# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3)) # 리스트 입력시 이어서 작업 하기 위함


#바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f) #loads 문자열 역직렬화
    print(type(b), 'Binary Read1 | ', b)
    b = pickle.load(f) #loads 문자열 역직렬화
    print(type(b), 'Binary Read2 | ', b)
    b = pickle.load(f) #loads 문자열 역직렬화
    print(type(b), 'Binary Read3 | ', b)

#텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read' + str(i) + ' | ', line,end='') #end='' 공백 처리
