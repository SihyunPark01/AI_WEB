#입력 : 키보드로 입력하는 방법 배워보자!
#출력 : print()함수로 모니터에 출력하는 방법 배웠지!

name = input('name :')
message = 'hi, '+name+' .... bye, '+name+'.'
print(message)
f = open("result1.txt",'w')
f.write(message)
f.close()


가격 = float(input('가격?'))
부가가치세율 = 0.1
부가가치세 = 가격*부가가치세율
print(부가가치세)
열린파일 = open("results.txt", 'a')
열린파일.write(str(부가가치세)+'\n')
열린파일.close()