def conv(ch):
	if ch == 'T': return 'U'
	else: return ch
with open("in.txt","r") as f:
	s = f.readlines()[0].strip()
	print ''.join([conv(x) for x in s])
