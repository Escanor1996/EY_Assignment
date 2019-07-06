Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def pos(n):
	white=[random.randint(1,n),random.randint(1,n)]
	black=[random.randint(1,n),random.randint(1,n)]
	return white,black

>>> def dis(n):
	white,black=pos(n)
	print(white)
	print(black)
	if white[0]==black[0]:
		min=abs(white[1]-black[1])
	if white[1]==black[1]:
		min=abs(white[0]-black[0])
	if (white[0]==white[1] and black[0]==black[1]):
		min=abs(white[1]-black[1])
	else:
		min1=abs(black[0]-white[0])
		if (white[1]+min1<n):
			min=min1+ abs(black[1]-(white[1]+min1))
		else:
			min=min1+ abs(black[1]-(white[1]-min1))

>>> dis(9)
[4, 1]
[5, 7]
>>> def dis(n):
	white,black=pos(n)
	print(white)
	print(black)
	if white[0]==black[0]:
		min=abs(white[1]-black[1])
	if white[1]==black[1]:
		min=abs(white[0]-black[0])
	if (white[0]==white[1] and black[0]==black[1]):
		min=abs(white[1]-black[1])
	else:
		min1=abs(black[0]-white[0])
		if (white[1]+min1<n):
			min=min1+ abs(black[1]-(white[1]+min1))
		else:
			min=min1+ abs(black[1]-(white[1]-min1))
	return min

>>> dis(9)
[4, 7]
[7, 5]
4
>>> 
