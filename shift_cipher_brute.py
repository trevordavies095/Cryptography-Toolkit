# File	: shift_cypher_brute.py
# Author: Trevor Davies
# Date	: September 5th, 2019

import sys

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Open file, no error checking cause I'm a bad programmer
with open(sys.argv[1]) as f:
	
	# Convert the file into a string
	data = f.read().strip().strip()

	# For every letter in the alphabet
	for key in range(len(letters)):
		translated = ""
		
		# For every letter in the cipher text
		for letter in data:
			
			# Check to see if it's a letter
			if letter.upper() in letters:
				
				# Grab the key
				num = letters.find(letter.upper())
				num = num - key

				# Handle case where we need to wrap
				if num < 0: 
					num = num + len(letters)

				# Add shifted letter to string
				translated = translated + letters[num]

			# Not a letter, but a symbol, just add it to the string
			else:
				translated = translated + letter

		# Print out the key shift and the text based on the key
		print("k=" + str(key) + ": " + translated)


