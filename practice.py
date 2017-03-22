"""
import statistics

x_array = [50,100,200,300]
y_array = [50,70,70,95]

a = statistics.stdev(x_array)
b = statistics.stdev(y_array)

print (a)
print (b)
"""

"""
str = "i Am The King Of These jungle"
str1 = str.split(' ',4)
print str1[0]
print str1[1]
print str1[2]
print str1[3]
print str1[4]

print str.capitalize()
print str.center(30,'2')



#if str.isalnum() == True:
#	print 'nitya'
"""
	
"""
def palindrom1(str):
	length = len(str)
	str1 = ''

	for char in str:
		str1 = char + str1
	print 'The palindrom is:', str1
str = raw_input('Enter a string: ')
palindrom1('apple')
"""

"""#family = ["Nitya","Aparna","Avni","Archita"]

for name in ["Nitya","Aparna","Avni","Archita"]:
	print name
"""

"""
def calc(a,b,o):
	if o == '+':
		return a + b
	elif o == '-':
		return a - b
	elif o == '*':
		return a * b
	elif o == '/':
		return a / float(b)
	elif o == '%':
		return a % b
print calc(10,4,'+')
print calc(10,4,'-')
print calc(10,4,'*')
print calc(10,4,'/')
print calc(10,4,'%')
"""

"""
import math
def prime(a):
	i = a # A number upto which you want to know the prime numbers
	m = 0
	for j in range(2,i + 1):
		k = int(math.sqrt(j))
		bool = 0
		for l in range(2,k + 1):
			if j % l == 0:
				bool = 1
				break
		if bool == 0:
			print (j)
			m = m + 1
	print (a, m)

for i in range(100,201):
	if i % 10 == 0:
		prime(i)
"""	


"""
rawstr = raw_input('Enter a number: ')

try:
	ival = int(rawstr)
except:
	ival = -1

if ival > 0:
	print 'Nice work'
else:
	print 'Not a number'
"""

"""
i = raw_input('Enter a number: ')
try:
	j = int(i)
	print 'nice job'
except:
	print 'bad input'
"""
	
"""
str = "123"
try:
	i = int(str)
except:
	i = 10
print i
"""
"""
import math
i = 25 # A number upto which you want to know the prime numbers
m = 0
for j in range(2,i + 1):
	k = int(math.sqrt(j))
	bool = 0
	for l in range(2,k + 1):
		if j % l == 0:
			bool = 1
			break
	if bool == 0:
		print j
		m = m + 1
print 'There are total', m,'prime numbers'
"""

"""
for i in range(5):
	print 'i = ',i
	if i > 2:
		print 'i is greater then 2'
"""
"""
n = 5

while n > 0:
	print n
	n = n - 1
	
print n
print 'blastoff!'

"""
"""
x = 11
if x < 10:
	print "small"
if x > 20:
	print "big"
print "finish"
"""
