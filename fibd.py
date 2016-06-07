with open("in.txt","r") as f:
	line = map(int,f.readlines()[0].strip().split())
	n = line[0]
	m = line[1]
	pop = [1] + [0]*(m-1)
	for i in range(n-1):
		pop = [sum(pop[1:])] + pop[:-1]
	print sum(pop)
