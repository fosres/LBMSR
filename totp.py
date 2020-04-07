import random

#Generate a 32-bit random key

i = 0
n = 0
list = []
for i in range(30000):
	n = random.randint(0,999999)
	while i < len(list):
		if list[i] == n:
			n = random.randint(0,999999)
			i = -1
		i += 1
	list.append(n)
	print(n)
