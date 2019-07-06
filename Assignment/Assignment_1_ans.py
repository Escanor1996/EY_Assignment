Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_subs(s):
	return [s[i:i+j] for j in range (1,len(s)+ 1) for i in range (len(s)-j+1)]

>>> def game(a):
	vowels = {'A', 'I', 'O', 'U', 'E', 'a', 'i', 'o', 'u', 'e'}
	vow_subs=[t for t in find_subs(a) if t[0] in vowels]
	con_subs=[t for t in find_subs(a) if t[0] not in vowels]
	if (len(con_subs)>len(vow_subs)):
		print("A has won with"+ " " +str(len(con_subs))+" "+"points")
	if (len(vow_subs)>len(con_subs)):
		print("B has won with"+ " "+str(len(vow_subs))+ " "+"points")
	if(len(con_subs)==len(vow_subs)):
		print("both end in a draw with"+ " "+str(len(vow_subs))+ " "+"points")

>>> a="banana"
>>> game(a)
A has won with 12 points
>>> a="ihsvbslnvlbajnvklsnblishgklkavbcajnvaevbalknlan"
>>> game(a)
A has won with 955 points
>>> 
