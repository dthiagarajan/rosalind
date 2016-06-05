def binomial(n, k):
    """Compute n factorial by a direct multiplicative method."""
    if k > n - k:
        k = n - k  # Use symmetry of Pascal's triangle
    accum = 1
    for i in range(1, k + 1):
        accum *= (n - (k - i))
        accum /= i
    return accum

def P(n,k):
	return binomial(2**k, n) * 0.25**n * 0.75**(2**k - n)
with open("in.txt","r") as f:
	nums = f.readlines()[0].strip().split()
	k = int(nums[0])
	N = int(nums[1])
	print (1 - sum([P(n,k) for n in range(N)]))
