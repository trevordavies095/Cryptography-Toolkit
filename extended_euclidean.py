# File	: extended_euclidean.py
# Author: Trevor Davies
# Date	: October 8th, 2019

import sys

def gcd_extended(r, s, t):
	# Local constants

	# Local variables
	i = 1
	q = [0]

	#****** start gcd_extended() ******#

	while True:
		i += 1
		r.insert(i, r[i-2] % r[i-1])
		q.insert(i-1, (r[i-2] - r[i]) / r[i-1])
		s.insert(i, s[i-2] - q[i-1] * s[i-1])
		t.insert(i, t[i-2] - q[i-1] * t[i-1])

		if(r[i] == 0): break

	# [gcd, x1, y1]
	return [int(r[i-1]), int(s[i-1]), int(t[i-1])]




s = []
s.insert(0, 1)
s.insert(1, 0)

t = []
t.insert(0, 0)
t.insert(1, 1)

a = sys.argv[1]
b = sys.argv[2]

r = []
r.insert(0, int(a))
r.insert(1, int(b))

ret = gcd_extended(r, s, t)
if(ret[1] < 0): ret[1] = ret[1] % r[1] 
if(ret[2] < 0): ret[2] = ret[2] % r[0] 

print("gcd(" + a + ", " + b + ") = " + str(ret[0]))
print(str(ret[1]) + " \N{IDENTICAL TO} " + str(a) + "^-1 mod " + str(b))
print(str(ret[2]) + " \N{IDENTICAL TO} " + str(b) + "^-1 mod " + str(a))