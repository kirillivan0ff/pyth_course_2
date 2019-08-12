def unique(arr):
	unique_arr = []
	
	for x in arr:
		if x not in unique_arr:
			unique_arr.append(x)
	return unique_arr