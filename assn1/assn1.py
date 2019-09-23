import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
	if n <= 1:
		return n
	
	else:


		num1 = 0
		num2 = 1
		for i in range(n-1):
			c = num1 + num2
			num1 = num2
			num2 = c
		return c

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

