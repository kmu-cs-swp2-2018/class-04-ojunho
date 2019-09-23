import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
#기존의 코드는 문자를 세개 사용하여 num1, num2, 그리고 c의 값을 바꿔가면서 마지막 실행에서 더해진 값을 리턴했지만 새로운 코드에서는 문자를 두개 사용하여
#그나마 더 적은 메모리를 사용하여 기능을 수행할 수 있다. 
# 또 range()안의 범위도 그냥 n으로 바뀌면서 횟수와 같기 때문에 조금 더 직관적으로 바뀌었다.
# a와 b의 값을 1, 0 으로 설정해 줌으로써 원래 코드의 앞에서 썼던 if 조건문을 사용하지 않아도 되고, 그로인해 효율이 더 높아진다.
	
	a, b = 1, 0
	for i in range(n):
		a, b = b, a + b
	return b

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))

