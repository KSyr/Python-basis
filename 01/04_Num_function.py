#숫자형(내장 함수)

#크기 비교 함수
print(max(5,8,-5,3)) #max()는 큰 값 : 8
print(min(5,8,-5,2)) #min()는 작은 값 :-5

#연산 함수 및 연산자

#sum([x,y...]) : [ ]안의 모든 값을 더하는 함수
print(sum([1,2,3,4,5]))   # 1+2+3+4+5

#pow(x,y) : x의 y제곱 값을 구하는 함수
print(pow(2,5))   #2^5제곱
#거듭제곱 연산자:  **
print(3**4)

#divmod(x,y) : x를 y로 나눈 후 몫,나머지 출력 함수
print(divmod(10,3))
print(10//3,10%3)

#round(x.y,z) : 소수 x.y를 소수자리 z+1자리에서 반올림하여 나타내는 함수

print(round(6.26,1)) #6.3
print(round(1.12,2)) #1.12
print(round(5/3,3))      #1.667

#abs(x) : x 절대값
print(abs(5))
print(abs(-5))  
