#!/usr/bin/env python

def funtest(n):
	result=0
	for i in range(n+1):
		result +=i
	return result

if __name__=='__main__':
	result = funtest(10)
	print(result)
