#! C:\python27

import string, random

#============ Word List Gen ============
minimum = 0
maximum = 9
wmaximum =input('Please enter the max number of words to be generate in the dictionary: ')

alphabet = string.letters[0:52] + string.digits + string.punctuation

string = ''
FILE = open("wl.txt", "w")
while (string !='Roy'):
	for count in xrange(0, wmaximum):
		for x in random.sample(alphabet, random.randint(minimum, maximum)):
			string += x
			FILE.write(string + '\n')
			string = ''
		FILE.close()
print 'DONE!'


