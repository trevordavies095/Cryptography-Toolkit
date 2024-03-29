# Cryptography Toolkit
This is a collection of scripts and algorithms I've written for my cryptography course (CSCI-462) at Rochester Institute of Technology.

## euclidean.py
Used to find the gcd of two numbers

`python euclidean.py a b`

## extended_euclidean.py
Used to compute gcd and modular inverses

`python extended_euclidean.py a b`

## freq.py
Used for a frequency analysis attack on a substitution cipher. You can compare the output of the script to [Wikipedia's chart on letter frequency](https://en.wikipedia.org/wiki/Letter_frequency).

`python freq.py cipher_text.txt`

## shift_cipher_brute.py
You can use this script to brute force a shift cipher.

`python shift_cipher_brute.py cipher_text.txt`
