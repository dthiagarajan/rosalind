with open("in.txt", "r") as f:
	s = f.readlines()[0].strip()
	ac = 0
	cc = 0
	gc = 0
	tc = 0
	for c in s:
		if c == 'A': ac += 1
		elif c == 'C': cc += 1
		elif c == 'G': gc += 1
		else: tc += 1
	print str(ac) + " " + str(cc) + " " + str(gc) + " " + str(tc)
