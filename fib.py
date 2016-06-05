def rec_count(x, acc, k, n_2, n_1):
	if x == 0: return acc
	else: return rec_count(x-1, (k*n_2) + n_1, k, n_1, (k*n_2) + n_1)
with open("in.txt","r") as f:
	nums = map(int, f.readlines()[0].strip().split())
	print rec_count(nums[0] - 2,1,nums[1],1,1)
