def check_factor(new_even, new_odd):
	e_rem = new_even%2
	o_rem = new_odd%3
	e_div = new_even/2
	o_div = new_odd/3
	if e_rem == 0 and o_rem == 0 and e_div == o_div:
		return 0
	common = (e_div + o_div + 1) / 2
	factor = 0
	if e_div < common:
		factor = 2*common - new_even
		div = (new_odd - factor)/3
		rem = (new_odd - factor)%3
		if div == common and  rem == 0: 
			return factor
		else:
			return -1
	if o_div < common:
		factor = 3*common - new_odd
		div = (new_even - factor)/2
		rem = (new_even - factor)%2
		if div == common and  rem == 0: 
			return factor
	return -1

def find_ops(even, odd):
	for i in range(len(even)):
		print check_factor(even[i], odd[i])


cases = int(raw_input())
e, o = [], []
while cases > 0:
	even, odd = raw_input().split(' ')
	e.append(long(even))
	o.append(long(odd))
	cases -= 1
find_ops(e, o)
