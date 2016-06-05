with open("in.txt","r") as f:
	lines = f.readlines()
	l1 = lines[0].strip()
	l2 = lines[1].strip()
	ct = 0
	for i in range(0,len(l1)):
		if l1[i] != l2[i]:
			ct += 1
	print ct	
