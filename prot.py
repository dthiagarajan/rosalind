rna_to_prot = {}
with open("rna_to_prot.txt","r") as f:
	lines = f.readlines()
	for l in lines:
		ll = l.split("      ")
		for p in ll:
			pp = p.split()
			if len(pp) == 4:
				rna_to_prot[pp[2].strip()] = pp[3].strip()
			rna_to_prot[pp[0].strip()] = pp[1].strip()
with open('in.txt','r') as f:
	s = f.readlines()[0].strip()
	s = s[s.index('AUG'):]
	out = ""
	while (rna_to_prot[s[0:3]] != 'Stop'):
		
		out += rna_to_prot[s[0:3]]
		s = s[3:]
	print out
