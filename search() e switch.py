def search(palavra, l):
	c=0
	positions=[]
	for n in palavra:
		if n==l:
			positions.append(c)
		c=c+1
	return positions
	
def switch(n, x, y):
	i1=search(n, x)
	i2=search(n, y)
	lista=[]
	for k in n:
		lista.append(k)
	for k in i1:
		lista[k]=y
	for k in i2:
		lista[k]=x
	n=""
	for k in lista:
		n=n+k
	return n