with open("in.txt","r") as f:
	nums = f.readlines()[0].strip().split()
	k = int(nums[0])
	m = int(nums[1])
	n = int(nums[2])
	p = k + m + n
	fl = ((4*k*(k-1)) + (3*m*(m-1)) + (4*((2*k*m) + (2*k*n) + (m*n)))) * 1.0/(4*p*(p-1))
	print fl
