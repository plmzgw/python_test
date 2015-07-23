#!/usr/bin/env python

def myfun1(n):
	result=0
	for i in range(n+1):
		result +=i
	return result

def myfun2():
	ll=[1, 2]
	print(ll[3])

if __name__=='__main__':
	result = myfun1(10)
	print(result)
