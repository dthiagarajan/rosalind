def conv(ch):
	if ch == 'A': return 'T'
	elif ch == 'T': return 'A'
	elif ch == 'G': return 'C'
	else: return 'G'
with open("in.txt","r") as f:
	print ''.join([conv(x) for x in f.readlines()[0].strip()[::-1]])
	
