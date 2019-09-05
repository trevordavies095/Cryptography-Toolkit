# File	: freq.py
# Author: Trevor Davies
# Date	: September 5th, 2019

import sys

count = 0
freq_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 
			'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 
			'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 
			'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

# Open file, no error checking cause I'm a bad programmer
with open(sys.argv[1]) as f:

	# Convert the file into a string, remove spaces because we don't care
	data = f.read().strip().replace(" ", "").lower()
	
	# Loop through the letter and update the dict and count
	for i in data:
		freq_dict[i] += 1
		count += 1

# Sort the dictionary by value, reverse the order
freq = sorted(freq_dict, key=freq_dict.get, reverse=True)

# Output
print("Letter\t\tCount\t\tFrequency")
for letter in freq:
	print(letter + "\t\t" + str(freq_dict[letter]) + "\t\t" + "%.3f" % ((freq_dict[letter]/count)*100))
