#과제 : 1 부터 10까지 반복하는 과정에서 3의 배수일경우, year를 출력하시오.
#나머지 모든 경우는 숫자 그대로 출력
for i in range(1,21):
    if i % 3 == 0:
        print('year')
    else:
        print(i)
