with open("in.txt","r") as f:
	nums = map(int,f.readlines()[0].split())
	print str((2.0*nums[0]) + (2.0*nums[1]) + (2.0*nums[2]) + (1.5*nums[3]) + (1.0*nums[4]))
