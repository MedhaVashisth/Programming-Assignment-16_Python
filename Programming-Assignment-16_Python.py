#!/usr/bin/env python
# coding: utf-8

# In[1]:


def stutter(word):
    s = word[:2]
    return (2 * (s + '... ')) + word + '?'


print(stutter("incredible"))


# In[2]:


# Python code to convert radian to degree

# Function for conversion
def Convert(radian):
	pi = 3.14159
	# Simply used the formula
	degree = radian * (180/pi)
	return degree

# Driver Code
radian = 5
print("degree =",(Convert(radian)))


# In[4]:


# Python3 implementation of the approach

# Function to check if a number
# is a Curzon number or not
def checkIfCurzonNumber(N):

	powerTerm, productTerm = 0, 0

	# Find 2^N + 1
	powerTerm = pow(2, N) + 1

	# Find 2*N + 1
	productTerm = 2 * N + 1

	# Check for divisibility
	if (powerTerm % productTerm == 0):
		print("Yes")
	else:
		print("No")

# Driver code
if __name__ == '__main__':
	
	N = 5
	checkIfCurzonNumber(N)

	N = 10
	checkIfCurzonNumber(N)



# In[8]:


# Python3 program to find
# area of a Hexagon
import math

# Function for calculating
# area of the hexagon.
def hexagonArea(s):
	
	return ((3 * math.sqrt(3) *
			(s * s)) / 2);
	
# Driver code	
if __name__ == "__main__" :

	# length of a side.
	s = 4

	print("Area:","{0:.4f}" .
		format(hexagonArea(s)))



# In[9]:


# Python program to convert a
# number from any base to decimal

# To return value of a char.
# For example, 2 is returned
# for '2'. 10 is returned for 'A',
# 11 for 'B'
def val(c):
	if c >= '0' and c <= '9':
		return ord(c) - ord('0')
	else:
		return ord(c) - ord('A') + 10;

# Function to convert a number
# from given base 'b' to decimal
def toDeci(str,base):
	llen = len(str)
	power = 1 #Initialize power of base
	num = 0	 #Initialize result

	# Decimal equivalent is str[len-1]*1 +
	# str[len-2]*base + str[len-3]*(base^2) + ...
	for i in range(llen - 1, -1, -1):
		
		# A digit in input number must
		# be less than number's base
		if val(str[i]) >= base:
			print('Invalid Number')
			return -1
		num += val(str[i]) * power
		power = power * base
	return num
	
# Driver code
strr = "11A"
base = 16
print('Decimal equivalent of', strr,
			'in base', base, 'is',
				toDeci(strr, base))



# In[ ]:




