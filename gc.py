def split(ll):
	started = False
	id = ""
	s = ""
	entries = []
	for l in ll:
		if (l[0] == ">"):
			if (started): entries.append((id,s))
			else: started = True
			id = l[1:].strip()
			s = ""
		else:
			s += l.strip()
	entries.append((id,s))
	return entries
		
def count(s):
	ct = 0
	for c in s: 
		if (c == 'G' or c == 'C'): ct += 1
	return (1.0 * ct)/(len(s))
with open("in.txt", "r") as f:
	max_id = ""
	max_count = -1.0
	for l in split(f.readlines()):
		print l
		c = count(l[1])
		if (c > max_count):
			max_id = l[0]
			max_count = c
	print max_id
	print float(max_count)*100.0
		
