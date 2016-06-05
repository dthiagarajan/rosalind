with open("rosalind_subs.txt","r") as f:
	lines = f.readlines()
	s = lines[0].strip()
	sub = lines[1].strip()
	out = ""
	for a in range(0,len(s) - len(sub) + 1):
		if s[a:a+len(sub)] == sub:
			out += str(a+1)
			out += " "
	print out
