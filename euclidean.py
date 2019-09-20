# File	: euclidean.py
# Author: Trevor Davies
# Date	: September 20th, 2019

import sys


def gcd(a, b):
	if a == 0:
		return b;
	return gcd(b % a, a)


a = sys.argv[1]
b = sys.argv[2]
print("gcd(" + a + ", " + b + ") = " + str(gcd(int(a), int(b))))
