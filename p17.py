def ntos(x):
	w1dict = {	1:'one',
				2:'two',
				3:'three',
				4:'four',
				5:'five',
				6:'six',
				7:'seven',
				8:'eight',
				9:'nine'
				}
	specialdict={11:'eleven',12:'twelve',
	13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
	17:'seventeen',18:'eighteen',19:'nineteen',1000:'onethousand'
	}
	w2dict = {	1:'ten',
				2:'twenty',
				3:'thirty',
				4:'forty',
				5:'fifty',
				6:'sixty',
				7:'seventy',
				8:'eighty',
				9:'ninety'
				}
	if x in specialdict:
		return specialdict[x]
	word=''
	if x//100>0:
		word+=w1dict[x//100]+'hundred'
		x=x%100
	if x==0:
		return word
	if word!='':
		word+='and'
	if x in specialdict:
		word+=specialdict[x]
		return word
	if x//10>0:
		word+=w2dict[x//10]
		x=x%10
	if x>0:
		word+=w1dict[x]
	return word

N=1000
s=''
for i in range(1,N+1):
	s+=ntos(i)
print(len(s))