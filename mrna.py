prot_to_rna = {}
def add(k):
	if k in prot_to_rna:
		prot_to_rna[k] = prot_to_rna[k] + 1
	else:
		prot_to_rna[k] = 1
with open("rna_to_prot.txt","r") as f:
        lines = f.readlines()
        for l in lines:
                ll = l.split("      ")
                for p in ll:
                        pp = p.split()
                        if len(pp) == 4:
				add(pp[3].strip())
			add(pp[1].strip())
with open("in.txt","r") as f:
	s = f.readlines()[0].strip()
	count = prot_to_rna['Stop']
	for c in s:
		count *= prot_to_rna[c]
		count %= 1000000
	print count
